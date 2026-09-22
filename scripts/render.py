#!/usr/bin/env python3
"""Renderiza um HTML de e-mail e devolve o que o olho veria.

O ciclo de design da suite depende disto: sem render, o HTML sai sem
ninguem olhar, e defeito visual nao tem ID de lint.

Saidas em `evals/render/<nome>/`:

    desktop-600.png   600 px de largura, pagina inteira
    mobile-375.png    375 px, viewport de celular
    dark-600.png      prefers-color-scheme: dark MAIS inversao forcada,
                      que e o que o app do Gmail faz em muitos aparelhos
    relatorio.json    altura, peso, imagens quebradas, primeira dobra
    relatorio.md      o mesmo, legivel

Uso:
    python3 scripts/render.py peca.html
    python3 scripts/render.py peca.html --nome campanha-x
    python3 scripts/render.py peca.html --json
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SAIDA_PADRAO = RAIZ / "evals" / "render"

# O app do Gmail em varios aparelhos nao respeita color-scheme: ele inverte
# o documento. Emular so `prefers-color-scheme` esconde metade dos defeitos.
CSS_INVERSAO_FORCADA = """
html { filter: invert(1) hue-rotate(180deg); background: #000 !important; }
img, video, svg, [style*="background-image"] { filter: invert(1) hue-rotate(180deg); }
"""

JS_METRICAS = """
() => {
  const doc = document.documentElement;
  const quebradas = [...document.images]
    .filter(i => !i.complete || i.naturalWidth === 0)
    .map(i => i.getAttribute('src') || '(sem src)');
  const semAlt = [...document.images]
    .filter(i => !i.hasAttribute('alt'))
    .map(i => i.getAttribute('src') || '(sem src)');
  const larguras = [...document.querySelectorAll('table,td,div')]
    .map(e => e.getBoundingClientRect().width)
    .filter(w => w > 300);
  const botoes = [...document.querySelectorAll('a')]
    .filter(a => {
      const r = a.getBoundingClientRect();
      return r.height >= 30 && r.width >= 80;
    })
    .map(a => {
      const r = a.getBoundingClientRect();
      return { texto: (a.innerText || '').trim().slice(0, 40),
               topo: Math.round(r.top + window.scrollY),
               altura: Math.round(r.height) };
    });
  return {
    altura_px: Math.max(doc.scrollHeight, document.body.scrollHeight),
    largura_max: larguras.length ? Math.round(Math.max(...larguras)) : null,
    imagens: document.images.length,
    imagens_quebradas: quebradas,
    imagens_sem_alt: semAlt,
    botoes: botoes,
  };
}
"""


# O ambiente ja traz o Chromium. A versao do pacote pip pode nao bater com
# a build instalada, e nesse caso o launch padrao falha pedindo download.
# Procurar o binario existente evita 'playwright install', que o ambiente
# pede para nao rodar.
CANDIDATOS_CHROMIUM = [
    "chromium-*/chrome-linux/chrome",
    "chromium_headless_shell-*/chrome-linux/headless_shell",
    "chromium/chrome-linux/chrome",
]


def acha_chromium() -> str | None:
    forcado = os.environ.get("PLAYWRIGHT_CHROMIUM")
    if forcado and Path(forcado).is_file():
        return forcado
    base = Path(os.environ.get("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers"))
    if not base.is_dir():
        return None
    for padrao in CANDIDATOS_CHROMIUM:
        # a build mais nova primeiro, quando houver mais de uma
        for c in sorted(base.glob(padrao), reverse=True):
            if c.is_file() and os.access(c, os.X_OK):
                return str(c)
    return None


def _navegador(p):
    """Abre o Chromium que ja vem no ambiente, sem baixar nada."""
    caminho = acha_chromium()
    if caminho:
        return p.chromium.launch(executable_path=caminho)
    return p.chromium.launch()


def renderiza(html_path: Path, nome: str | None = None,
              saida: Path | None = None) -> dict:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        raise SystemExit(
            "playwright nao instalado. Rode:\n"
            "  python3 -m pip install playwright\n"
            "O Chromium ja existe no ambiente (PLAYWRIGHT_BROWSERS_PATH), "
            "nao rode 'playwright install'."
        )

    html_path = Path(html_path).resolve()
    nome = nome or html_path.stem
    dest = Path(saida) if saida else SAIDA_PADRAO / nome
    dest.mkdir(parents=True, exist_ok=True)

    url = html_path.as_uri()
    peso_kb = html_path.stat().st_size / 1024
    rel: dict = {"nome": nome, "fonte": str(html_path),
                 "peso_kb": round(peso_kb, 1), "capturas": {}}

    with sync_playwright() as p:
        nav = _navegador(p)

        # desktop 600, a largura real do e-mail
        ctx = nav.new_context(viewport={"width": 600, "height": 900},
                              device_scale_factor=2)
        pg = ctx.new_page()
        pg.goto(url, wait_until="networkidle")
        m = pg.evaluate(JS_METRICAS)
        rel.update(m)
        pg.screenshot(path=str(dest / "desktop-600.png"), full_page=True)
        rel["capturas"]["desktop"] = "desktop-600.png"

        # primeira dobra: o que aparece sem rolar, em 600x900
        rel["primeira_dobra_px"] = 900
        rel["cta_na_primeira_dobra"] = any(
            b["topo"] < 900 for b in m.get("botoes", []))
        ctx.close()

        # mobile 375
        ctx = nav.new_context(viewport={"width": 375, "height": 667},
                              device_scale_factor=2, is_mobile=True,
                              has_touch=True)
        pg = ctx.new_page()
        pg.goto(url, wait_until="networkidle")
        mm = pg.evaluate(JS_METRICAS)
        pg.screenshot(path=str(dest / "mobile-375.png"), full_page=True)
        rel["capturas"]["mobile"] = "mobile-375.png"
        rel["mobile"] = {
            "altura_px": mm["altura_px"],
            "largura_max": mm["largura_max"],
            # rolagem horizontal e defeito: o e-mail tem que caber
            "rola_horizontal": bool(mm["largura_max"] and mm["largura_max"] > 375),
            "cta_na_primeira_dobra": any(b["topo"] < 667 for b in mm.get("botoes", [])),
        }
        ctx.close()

        # dark: prefers-color-scheme MAIS inversao forcada
        ctx = nav.new_context(viewport={"width": 600, "height": 900},
                              device_scale_factor=2, color_scheme="dark")
        pg = ctx.new_page()
        pg.goto(url, wait_until="networkidle")
        pg.add_style_tag(content=CSS_INVERSAO_FORCADA)
        pg.wait_for_timeout(150)
        pg.screenshot(path=str(dest / "dark-600.png"), full_page=True)
        rel["capturas"]["dark"] = "dark-600.png"
        ctx.close()

        nav.close()

    rel["avisos"] = _avisos(rel)
    (dest / "relatorio.json").write_text(
        json.dumps(rel, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (dest / "relatorio.md").write_text(_markdown(rel, dest), encoding="utf-8")
    return rel


def _avisos(r: dict) -> list[str]:
    """O que o render mede e o lint estatico nao consegue ver."""
    a = []
    alt = r.get("altura_px") or 0
    if alt > 4000:
        a.append(f"R01 altura {alt} px: acima de 4.000, que e o valor que a "
                 f"carteira mediu como fracasso (o 11h do 9.9 tinha 4.136)")
    elif alt > 3200:
        a.append(f"R02 altura {alt} px: acima do alvo de 2.000 a 3.200")
    elif alt and alt < 800:
        a.append(f"R03 altura {alt} px: peca muito curta, confira se nao "
                 f"faltou secao")
    if r.get("peso_kb", 0) > 102:
        a.append(f"R04 peso {r['peso_kb']} KB: acima de 102 KB, o Gmail corta")
    lm = r.get("largura_max")
    if lm and lm > 620:
        a.append(f"R05 largura {lm} px: o container passa de 600")
    if r.get("imagens_quebradas"):
        a.append(f"R06 {len(r['imagens_quebradas'])} imagem quebrada: "
                 + ", ".join(r["imagens_quebradas"][:3]))
    if r.get("imagens_sem_alt"):
        a.append(f"R07 {len(r['imagens_sem_alt'])} imagem sem alt")
    if not r.get("cta_na_primeira_dobra"):
        a.append("R08 nenhum botao na primeira dobra do desktop (900 px)")
    mob = r.get("mobile", {})
    if mob.get("rola_horizontal"):
        a.append(f"R09 rolagem horizontal no mobile: largura {mob['largura_max']} px "
                 f"em viewport de 375")
    if not mob.get("cta_na_primeira_dobra"):
        a.append("R10 nenhum botao na primeira dobra do mobile (667 px)")
    return a


def _markdown(r: dict, dest: Path) -> str:
    av = "\n".join(f"- {x}" for x in r["avisos"]) or "- nenhum"
    mob = r.get("mobile", {})
    return f"""# Render: {r['nome']}

| | |
|---|---|
| Altura | **{r.get('altura_px')} px** |
| Peso | **{r['peso_kb']} KB** |
| Largura maxima | {r.get('largura_max')} px |
| Imagens | {r.get('imagens')} ({len(r.get('imagens_quebradas', []))} quebradas) |
| CTA na primeira dobra, desktop | {'sim' if r.get('cta_na_primeira_dobra') else 'NAO'} |
| CTA na primeira dobra, mobile | {'sim' if mob.get('cta_na_primeira_dobra') else 'NAO'} |
| Rola horizontal no mobile | {'SIM' if mob.get('rola_horizontal') else 'nao'} |

## Avisos

{av}

## Capturas

| Arquivo | O que e |
|---|---|
| `desktop-600.png` | 600 px, pagina inteira |
| `mobile-375.png` | 375 px, viewport de celular |
| `dark-600.png` | dark mode com inversao forcada, como o app do Gmail |

**Os PNGs precisam ser lidos, nao so gerados.** O ciclo de
`skills/email-design` manda olhar os tres antes de entregar.
"""


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("html")
    ap.add_argument("--nome")
    ap.add_argument("--saida")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    r = renderiza(Path(a.html), a.nome, Path(a.saida) if a.saida else None)
    if a.json:
        print(json.dumps(r, ensure_ascii=False, indent=2))
    else:
        print(_markdown(r, Path()))
    return 1 if r["avisos"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
