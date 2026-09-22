#!/usr/bin/env python3
"""Produz um lote de pecas a partir de um arquivo de briefs.

Por brief: copy -> estrutura -> HTML -> ciclo de render -> lint -> nota.

Saida em `out/<loja>/<data-hora>-<slug>/`:
    email.html  copy.json  desktop-600.png  mobile-375.png  dark-600.png
    relatorio.md

E `out/<loja>/index.html`, a galeria para aprovar tudo em uma tela.

Peca com violacao B, ou nota abaixo de 8, vai para `out/<loja>/_reprovados/`
com o motivo.

IMPORTANTE: este script monta o esqueleto e mede. **A nota que ele calcula
e mecanica**, derivada do lint e dos avisos de render. A nota do revisor
de verdade (`skills/email-revisor`) exige ler os PNGs em contexto limpo, e
isso e trabalho de agente, nao de script. O relatorio marca qual das duas
esta ali.

Uso:
    python3 scripts/produzir_lote.py --briefs <arquivo.json> --loja blue-wolf
    python3 scripts/produzir_lote.py --limite 5
"""

from __future__ import annotations

import argparse
import html as html_mod
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
BRIEFS_PADRAO = (RAIZ / "fontes" / "BFCM-2026-Convertfy" / "09_Dados"
                 / "Briefs_Q4_2026_Convertfy.json")
OUT = RAIZ / "out"

NOTA_MINIMA = 8


# ---------------------------------------------------------------------------
# Brief -> copy
# ---------------------------------------------------------------------------
def slugify(t: str, n: int = 52) -> str:
    t = re.sub(r"[^\w\s-]", "", t, flags=re.U).strip().lower()
    return re.sub(r"[\s_-]+", "-", t)[:n].strip("-")


# Os `blocos` do brief sao DESCRICAO DE ESTRUTURA, nao copy final:
# 'Hero: "QUER JOGAR UM JOGO?" + grade de 8 botoes com os codigos'.
# Despejar isso no corpo produz peca que mostra a instrucao para o cliente.
# A copy final sai das aspas dentro da descricao; o resto vira nota de
# estrutura, que nao entra no HTML.
RX_ASPAS = re.compile(r'"([^"]{3,})"')
RX_ROTULO = re.compile(
    r"^\s*(hero|assinatura|regra|bloco|grade|p\.?s\.?|onde testar|"
    r"instrucao|instrução|cta|botao|botão|rodape|rodapé)\b[^:]{0,26}:",
    re.IGNORECASE)
RX_CTA = re.compile(r'bot[aã]o[^"]{0,30}"([^"]{2,40})"', re.IGNORECASE)


# Alem do rotulo no inicio, a descricao de estrutura tem duas marcas:
# junta fragmentos com " + ", e nomeia componente ("grade 2x2", "botao unico").
RX_MONTAGEM = re.compile(
    r'"\s*\+|\+\s*"|\bgrade\s*\d?x?\d?\b|\bbot[aã]o\s+[uú]nico\b|'
    r'\bcada um com\b|\bcom os c[oó]digos\b',
    re.IGNORECASE)


def _copy_do_bloco(texto: str) -> list[str]:
    """Devolve a copy real de um bloco de brief, ou [] se for so estrutura."""
    if RX_MONTAGEM.search(texto):
        # e instrucao de montagem: so a frase entre aspas mais longa vale
        aspas = [a.strip() for a in RX_ASPAS.findall(texto)
                 if len(a.split()) >= 4]
        return aspas[:1]
    if RX_ROTULO.match(texto):
        aspas = [a.strip() for a in RX_ASPAS.findall(texto)]
        # frase entre aspas com mais de duas palavras e copy; token solto nao
        return [a for a in aspas if len(a.split()) >= 3]
    # bloco sem rotulo de estrutura ja e copy
    return [texto] if len(texto.split()) >= 3 else []


def copy_do_brief(b: dict, idioma: str) -> dict:
    """Extrai os campos de copy do brief, sem inventar nada.

    O que o brief nao traz sai como [FALTA: ...]: e P02, e o lint pega.
    """
    a = b.get("assunto") or {}
    cb = b.get("copy_base") or {}
    assunto = (a.get("en") if idioma == "en" else a.get("escolhido")) or \
              a.get("escolhido") or "[FALTA: assunto]"
    oferta = b.get("oferta", "")

    # ordem que a carteira manda: oferta e prazo antes de tudo, CTA logo apos
    blocos = []
    if cb.get("hero"):
        blocos.append(cb["hero"])
    if cb.get("subtitulo"):
        blocos.append(cb["subtitulo"])
    estrutura = []
    for x in (cb.get("blocos") or []):
        real = _copy_do_bloco(x)
        if real:
            blocos += real
        else:
            estrutura.append(x)

    # o CTA costuma estar dentro da descricao do bloco, entre aspas
    cta = cb.get("cta") or b.get("cta")
    if isinstance(cta, dict):
        cta = cta.get("texto")
    if not cta:
        for x in (cb.get("blocos") or []):
            m = RX_CTA.search(x)
            if m:
                cta = m.group(1).strip()
                break
    cta = cta or "[FALTA: cta]"
    blocos = [x for x in blocos if x.strip() and x.strip() != cta]

    nums = sorted(set(re.findall(r"\d+", oferta + " " + str(cb))))
    return {
        "idioma": idioma,
        "assunto": assunto,
        "preheader": a.get("preheader") or cb.get("subtitulo", "")[:120] or "",
        "blocos": [x for x in blocos if x],
        "ctas": [cta],
        "alts": [oferta[:100]] if oferta else [],
        "brief_numbers": nums,
        "marca_usa_emoji": True,
        "_oferta": oferta,
        "_papel": b.get("papel", ""),
        "_data": b.get("data", ""),
        "_hora": b.get("hora", ""),
        "_nome": b.get("nome", ""),
        "_estrutura": estrutura,
    }


# ---------------------------------------------------------------------------
# copy -> HTML
# ---------------------------------------------------------------------------
def monta_html(c: dict, ficha: dict) -> str:
    """Esqueleto valido: 600px, tabela, inline, bulletproof, dark seguro.

    Nao e a peca final de design: e o piso tecnico sobre o qual o ciclo de
    render trabalha.
    """
    e = html_mod.escape
    cor = ficha.get("cor_primaria", "#000000")
    txt = "#1A1A1A"
    fundo = "#FFFFFF"
    marca = ficha.get("nome", "LOJA").upper()
    blocos = "".join(
        f'<tr><td style="padding:0 24px 16px;font:16px/1.55 Helvetica,Arial,'
        f'sans-serif;color:{txt};">{e(b)}</td></tr>'
        for b in c["blocos"])
    cta = e(c["ctas"][0])
    # a carteira manda oferta, cupom, prazo e botao nos primeiros 500 px
    oferta = c.get("_oferta", "")
    oferta_html = (
        f'<tr><td class="pad" style="padding:0 24px 16px;font:bold 17px/1.45 '
        f'Helvetica,Arial,sans-serif;color:{cor};">{e(oferta)}</td></tr>'
        if oferta else "")
    return f"""<!doctype html>
<html lang="{c['idioma']}" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light dark">
<meta name="supported-color-schemes" content="light dark">
<title>{e(c['assunto'])}</title>
<!--[if mso]><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml><![endif]-->
<style>
  @media (max-width:620px) {{
    .wrap {{ width:100% !important; }}
    .pad {{ padding-left:16px !important; padding-right:16px !important; }}
  }}
</style>
</head>
<body style="margin:0;padding:0;background:{fundo};">
<div style="display:none;max-height:0;overflow:hidden;opacity:0;">{e(c['preheader'])}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:{fundo};">
<tr><td align="center">
<table role="presentation" class="wrap" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:600px;background:{fundo};">
  <tr><td class="pad" style="padding:22px 24px 18px;font:bold 13px Helvetica,Arial,sans-serif;letter-spacing:.09em;color:{cor};">{e(marca)}</td></tr>
  <tr><td class="pad" style="padding:0 24px 14px;font:bold 27px/1.22 Helvetica,Arial,sans-serif;color:{txt};">{e(c['assunto'])}</td></tr>
  {oferta_html}
  <tr><td align="center" style="padding:4px 24px 22px;">
    <!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="#" style="height:48px;v-text-anchor:middle;width:280px;" arcsize="4%" stroke="f" fillcolor="{cor}"><w:anchorlock/><center style="color:#FFFFFF;font-family:Helvetica,Arial,sans-serif;font-size:15px;font-weight:bold;">{cta}</center></v:roundrect><![endif]-->
    <!--[if !mso]><!--><a href="#" style="display:inline-block;background:{cor};color:#FFFFFF;font:bold 15px Helvetica,Arial,sans-serif;text-decoration:none;padding:16px 36px;min-width:200px;text-align:center;">{cta}</a><!--<![endif]-->
  </td></tr>
{blocos}
  <tr><td align="center" style="padding:10px 24px 26px;">
    <!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="#" style="height:48px;v-text-anchor:middle;width:280px;" arcsize="4%" stroke="f" fillcolor="{cor}"><w:anchorlock/><center style="color:#FFFFFF;font-family:Helvetica,Arial,sans-serif;font-size:15px;font-weight:bold;">{cta}</center></v:roundrect><![endif]-->
    <!--[if !mso]><!--><a href="#" style="display:inline-block;background:{cor};color:#FFFFFF;font:bold 15px Helvetica,Arial,sans-serif;text-decoration:none;padding:16px 36px;min-width:200px;text-align:center;">{cta}</a><!--<![endif]-->
  </td></tr>
  <tr><td class="pad" style="padding:18px 24px 26px;border-top:1px solid #E3E3E3;font:12px/1.6 Helvetica,Arial,sans-serif;color:#595959;">
    Voce recebe este e-mail porque se inscreveu na lista da {e(marca.title())}.
    <a href="#" style="color:#595959;">Descadastrar</a>.<br>
    {e(ficha.get('endereco', '[FALTA: endereco fisico do remetente]'))}
  </td></tr>
</table>
</td></tr></table>
</body></html>"""


# ---------------------------------------------------------------------------
# medicao
# ---------------------------------------------------------------------------
def roda(script: str, arq: Path) -> dict:
    r = subprocess.run([sys.executable, str(RAIZ / "scripts" / script),
                        "--json", str(arq)], capture_output=True, text=True)
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        return {"ok": False, "bloqueia": False, "total": 0, "violacoes": [],
                "_erro": (r.stderr or "")[-300:]}


def nota_mecanica(lc: dict, le: dict, rel: dict) -> tuple[int, list[str]]:
    """Nota derivada do que da para medir. NAO substitui o revisor.

    Regra igual a de shared/postura-revisao.md: B trava em 3, A tira 1,
    M tira 0,5 com teto de 2.
    """
    vs = lc.get("violacoes", []) + le.get("violacoes", [])
    b = [v for v in vs if v["severidade"] == "B"]
    a = [v for v in vs if v["severidade"] == "A"]
    m = [v for v in vs if v["severidade"] == "M"]
    av = rel.get("avisos", [])
    graves = [x for x in av if x[:3] in {"R01", "R04", "R06", "R09", "R10"}]
    motivos = []
    if b:
        motivos += [f"{v['regra']} (B)" for v in b]
    if graves:
        motivos += [g[:3] + " (render B)" for g in graves]
    if b or graves:
        return 3, motivos
    nota = 10 - len(a) - min(2, 0.5 * len(m)) - 0.5 * len(av)
    motivos = [f"{v['regra']} (A)" for v in a] + [x[:3] for x in av]
    return max(0, int(round(nota))), motivos


# ---------------------------------------------------------------------------
# lote
# ---------------------------------------------------------------------------
def carrega_ficha(loja: str) -> dict:
    f = RAIZ / "marcas" / f"{loja}.md"
    d = {"nome": loja.replace("-", " ")}
    if not f.is_file():
        return d
    t = f.read_text(encoding="utf-8")
    if t.startswith("---"):
        for l in t.split("---", 2)[1].splitlines():
            mm = re.match(r'^([a-z_]+):\s*"?([^"]*)"?$', l.strip())
            if mm:
                d[mm.group(1)] = mm.group(2)
    d["nome"] = loja.replace("-", " ").title()
    return d


def produz(brief: dict, loja: str, ficha: dict, idioma: str) -> dict:
    slug = slugify(brief.get("nome", "sem-nome"))
    carimbo = f"{brief.get('data','')}-{brief.get('hora','').replace(':','')}"
    dest = OUT / loja / f"{carimbo}-{slug}"
    dest.mkdir(parents=True, exist_ok=True)

    c = copy_do_brief(brief, idioma)
    (dest / "copy.json").write_text(
        json.dumps({k: v for k, v in c.items() if not k.startswith("_")},
                   ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (dest / "email.html").write_text(monta_html(c, ficha), encoding="utf-8")

    # ciclo de render
    rel = {}
    try:
        sys.path.insert(0, str(RAIZ / "scripts"))
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "render", RAIZ / "scripts" / "render.py")
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        rel = mod.renderiza(dest / "email.html", nome=slug, saida=dest)
    except Exception as exc:
        rel = {"avisos": [f"R00 render falhou: {exc}"], "erro": str(exc)}

    lc = roda("lint_copy.py", dest / "copy.json")
    le = roda("lint_email.py", dest / "email.html")
    nota, motivos = nota_mecanica(lc, le, rel)
    bloqueia = lc.get("bloqueia") or le.get("bloqueia")

    (dest / "relatorio.md").write_text(
        relatorio(brief, c, lc, le, rel, nota, motivos), encoding="utf-8")

    return {"slug": slug, "dir": dest, "nota": nota, "motivos": motivos,
            "bloqueia": bool(bloqueia), "rel": rel, "lc": lc, "le": le,
            "brief": brief, "copy": c}


def relatorio(b, c, lc, le, rel, nota, motivos) -> str:
    def tab(d):
        vs = d.get("violacoes", [])
        if not vs:
            return "- nenhuma\n"
        return "".join(f"- **{v['regra']}** ({v['severidade']}) `{v['campo']}`: "
                       f"{v['trecho'][:70]}\n" for v in vs)
    av = "\n".join(f"- {x}" for x in rel.get("avisos", [])) or "- nenhum"
    return f"""# {b.get('nome','')}

| | |
|---|---|
| Data | {b.get('data')} {b.get('hora')} |
| Papel | {b.get('papel','')} |
| Janela | {b.get('janela','')} |
| Oferta | {b.get('oferta','')} |
| **Nota mecânica** | **{nota}/10** |
| Bloqueia | {'SIM' if lc.get('bloqueia') or le.get('bloqueia') else 'não'} |

> A nota acima é **mecânica**, derivada do lint e dos avisos de render.
> Não substitui `skills/email-revisor`, que precisa ler os três PNGs em
> contexto limpo. Enquanto o revisor não passar, esta peça não está
> aprovada, só medida.

## Motivos

{chr(10).join('- ' + m for m in motivos) or '- nenhum'}

## Render

{av}

| | |
|---|---|
| Altura | {rel.get('altura_px')} px |
| Peso | {rel.get('peso_kb')} KB |
| CTA na dobra, desktop | {'sim' if rel.get('cta_na_primeira_dobra') else 'NÃO'} |
| CTA na dobra, mobile | {'sim' if (rel.get('mobile') or {}).get('cta_na_primeira_dobra') else 'NÃO'} |

## lint_copy

{tab(lc)}
## lint_email

{tab(le)}
## Próximo passo

1. Abrir `desktop-600.png`, `mobile-375.png` e `dark-600.png`.
2. Rodar o ciclo de `skills/email-design/references/ciclo-de-render.md`.
3. Passar pelo `email-revisor` em contexto limpo.
"""


def galeria(loja: str, pecas: list[dict]) -> str:
    cards = []
    for p in sorted(pecas, key=lambda x: (-x["nota"], x["slug"])):
        ok = not p["bloqueia"] and p["nota"] >= NOTA_MINIMA
        rel_dir = p["dir"].name if ok else f"_reprovados/{p['dir'].name}"
        cor = "#0a6b2e" if ok else "#a10000"
        motivos = ", ".join(p["motivos"][:4]) or "sem achados"
        cards.append(f"""
  <article style="border:1px solid #ddd;padding:14px;">
    <a href="{rel_dir}/desktop-600.png" style="display:block;">
      <img src="{rel_dir}/desktop-600.png" alt="{html_mod.escape(p['brief'].get('nome',''))}"
           style="width:100%;border:1px solid #eee;background:#fff;">
    </a>
    <h2 style="font-size:14px;margin:10px 0 4px;">{html_mod.escape(p['brief'].get('nome',''))}</h2>
    <p style="margin:0 0 6px;font-size:12px;color:#555;">
      {p['brief'].get('data')} {p['brief'].get('hora')} · {html_mod.escape(p['brief'].get('papel','')[:54])}</p>
    <p style="margin:0 0 6px;font-weight:700;color:{cor};font-size:13px;">
      {'APROVADA' if ok else 'REPROVADA'} · nota {p['nota']}/10</p>
    <p style="margin:0;font-size:12px;color:#666;">{html_mod.escape(motivos)}</p>
    <p style="margin:8px 0 0;font-size:12px;">
      <a href="{rel_dir}/relatorio.md">relatório</a> ·
      <a href="{rel_dir}/email.html">html</a> ·
      <a href="{rel_dir}/mobile-375.png">mobile</a> ·
      <a href="{rel_dir}/dark-600.png">dark</a></p>
  </article>""")
    ap = sum(1 for p in pecas if not p["bloqueia"] and p["nota"] >= NOTA_MINIMA)
    return f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8">
<title>Lote {html_mod.escape(loja)}</title>
<style>
 body{{margin:0;padding:26px;background:#fff;color:#000;
   font:14px/1.5 -apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;}}
 .grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:18px;}}
 h1{{font-size:18px;margin:0 0 4px;}} .sub{{color:#555;margin:0 0 20px;}}
</style></head><body>
<h1>Lote: {html_mod.escape(loja)}</h1>
<p class="sub">{len(pecas)} peças · <b>{ap} aprovadas</b> · {len(pecas)-ap} reprovadas ·
gerado em {datetime.now():%Y-%m-%d %H:%M}<br>
Reprova quem tem violação B ou nota abaixo de {NOTA_MINIMA}.
A nota é mecânica: o revisor em contexto limpo ainda não passou.</p>
<div class="grid">{''.join(cards)}
</div></body></html>"""


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--briefs", default=str(BRIEFS_PADRAO))
    ap.add_argument("--loja", default="blue-wolf")
    ap.add_argument("--idioma", default="pt-br")
    ap.add_argument("--limite", type=int, default=0)
    a = ap.parse_args(argv)

    dados = json.loads(Path(a.briefs).read_text(encoding="utf-8"))
    briefs = dados["emails"] if isinstance(dados, dict) else dados
    if a.limite:
        briefs = briefs[:a.limite]

    ficha = carrega_ficha(a.loja)
    destino = OUT / a.loja
    if destino.exists():
        shutil.rmtree(destino)
    (destino / "_reprovados").mkdir(parents=True, exist_ok=True)

    pecas = []
    for i, b in enumerate(briefs, 1):
        print(f"[{i}/{len(briefs)}] {b.get('nome','')[:56]}", flush=True)
        p = produz(b, a.loja, ficha, a.idioma)
        if p["bloqueia"] or p["nota"] < NOTA_MINIMA:
            alvo = destino / "_reprovados" / p["dir"].name
            shutil.move(str(p["dir"]), str(alvo))
            p["dir"] = alvo
            (alvo / "MOTIVO.txt").write_text(
                "Reprovada.\n" +
                ("Violacao B no lint.\n" if p["bloqueia"] else "") +
                (f"Nota {p['nota']} abaixo de {NOTA_MINIMA}.\n"
                 if p["nota"] < NOTA_MINIMA else "") +
                "\n".join(f"- {m}" for m in p["motivos"]) + "\n",
                encoding="utf-8")
        pecas.append(p)

    (destino / "index.html").write_text(galeria(a.loja, pecas), encoding="utf-8")
    ok = sum(1 for p in pecas if not p["bloqueia"] and p["nota"] >= NOTA_MINIMA)
    print(f"\n{len(pecas)} pecas | {ok} aprovadas | {len(pecas)-ok} reprovadas")
    print(f"galeria: {destino / 'index.html'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
