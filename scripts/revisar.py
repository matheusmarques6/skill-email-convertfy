#!/usr/bin/env python3
"""Torna o revisor executavel, sem fingir que um script julga a peca.

O que um script NAO faz: olhar os tres PNGs e decidir se a peca e boa.
Isso e trabalho de agente, e continua sendo.

O que este script faz, e que antes nao existia:

  --preparar   monta o pacote de contexto limpo: SO os tres PNGs e a ficha
               da marca. O HTML, o brief, a copy e a lista de correcoes
               ficam de fora, deliberadamente. Gera o formulario em branco
  --pontuar    le o formulario preenchido mais o lint, e calcula a nota
               pela regra de shared/postura-revisao.md. Deterministico
  --estado     diz se a peca ja foi revisada, e por qual versao do catalogo

A diferenca pratica: antes a revisao era prosa num SKILL.md e podia ser
pulada em silencio. Agora a peca nao fica aprovada sem `revisao.json`
preenchido, e o `produzir_lote` cobra.

Uso:
    python3 scripts/revisar.py --preparar out/blue-wolf/<peca>
    python3 scripts/revisar.py --pontuar  out/blue-wolf/<peca>
    python3 scripts/revisar.py --estado   out/blue-wolf/<peca>
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
NOTA_MINIMA = 8
TETO_SEM_QUALIDADE = 6

# Q1 a Q6 valem para toda peca. Fonte: shared/padrao-de-qualidade.md
PERGUNTAS_GERAIS = [
    ("Q1", "A oferta e a condicao aparecem sem rolar, no desktop e no mobile?"),
    ("Q2", "A peca diz um fato que so esta loja poderia dizer?"),
    ("Q3", "O papel do envio esta cumprido, lendo so a peca?"),
    ("Q4", "Existe uma acao unica e obvia?"),
    ("Q5", "A peca funciona com as imagens desligadas?"),
    ("Q6", "Alguem da loja assina, e essa pessoa existe?"),
]

PERGUNTAS_POR_PAPEL = {
    "antecipacao": [
        ("Q7a", "Traz uma noticia nova que os toques anteriores nao deram?"),
        ("Q8a", "Pede uma tarefa (votar, confirmar vaga, salvar favorito)?"),
        ("Q9a", "Nao repete a promessa do toque anterior?"),
        ("Q10a", "Diz o que acontece na data, nao so que algo vem?"),
    ],
    "pico": [
        ("Q7b", "O cupom esta visivel e colado no botao?"),
        ("Q8b", "O prazo tem data e hora?"),
        ("Q9b", "O formato bate com o horario (07h texto de pessoa, 18h estado)?"),
        ("Q10b", "A peca nao anuncia a proxima janela de oferta?"),
    ],
    "fechamento": [
        ("Q7c", "O prazo declarado e real e sera cumprido no ESP?"),
        ("Q8c", "Nao ha prorrogacao nem extensao anunciada?"),
        ("Q9c", "A urgencia vem de um fato, nao de adjetivo?"),
        ("Q10c", "Fecha de verdade, sem 'ainda da tempo' no dia seguinte?"),
    ],
    "ressaca": [
        ("Q7d", "Nao traz cupom novo entre um evento e o proximo?"),
        ("Q8d", "O aviso de estoque esta em fundo branco e texto preto?"),
        ("Q9d", "A reabertura vai so para quem clicou e nao comprou?"),
        ("Q10d", "Favoritos entre D+5 e D+8?"),
    ],
}

# O que o revisor NAO pode receber. Contexto limpo e a regra principal:
# quem sabe a intencao le a intencao, nao o resultado.
PROIBIDOS = {"email.html", "copy.json", "relatorio.md", "brief.json",
             "MOTIVO.txt", "correcoes.md"}


def _versao() -> str:
    try:
        import importlib.util
        s = importlib.util.spec_from_file_location(
            "vc", RAIZ / "scripts" / "versao_catalogo.py")
        m = importlib.util.module_from_spec(s)
        s.loader.exec_module(m)
        return m.versao()
    except Exception:
        return "cat-desconhecida"


def papel_da_peca(d: Path) -> str:
    """Le o papel do relatorio da peca, para escolher o bloco de perguntas."""
    rel = d / "relatorio.md"
    if not rel.is_file():
        return "pico"
    t = rel.read_text(encoding="utf-8", errors="replace").lower()
    for chave in ("antecipacao", "antecipação"):
        if chave in t:
            return "antecipacao"
    for chave, papel in (("fechamento", "fechamento"), ("ressaca", "ressaca"),
                         ("pos-pico", "ressaca"), ("pico", "pico")):
        if chave in t:
            return papel
    return "pico"


def preparar(d: Path) -> dict:
    d = d.resolve()
    pacote = d / "revisao"
    if pacote.exists():
        shutil.rmtree(pacote)
    pacote.mkdir(parents=True)

    levados, faltando = [], []
    for png in ("desktop-600.png", "mobile-375.png", "dark-600.png"):
        f = d / png
        if f.is_file():
            shutil.copy2(f, pacote / png)
            levados.append(png)
        else:
            faltando.append(png)

    # a ficha da marca e a unica coisa alem dos PNGs
    loja = d.parent.name if d.parent.name != "_reprovados" else d.parent.parent.name
    ficha = RAIZ / "marcas" / f"{loja}.md"
    if ficha.is_file():
        shutil.copy2(ficha, pacote / "ficha-da-marca.md")
        levados.append("ficha-da-marca.md")
    else:
        faltando.append(f"marcas/{loja}.md")

    papel = papel_da_peca(d)
    form = {
        "_leia": ("Responda sim ou nao. Sem meio-termo: se precisa de "
                  "ressalva, e nao. Olhe os tres PNGs antes."),
        "_contexto_limpo": ("Este pacote tem SO os PNGs e a ficha. O HTML, o "
                            "brief e a copy ficaram de fora de proposito: "
                            "quem sabe a intencao le a intencao, nao o "
                            "resultado."),
        "versao_catalogo": _versao(),
        "papel": papel,
        "respostas": {c: None for c, _ in
                      PERGUNTAS_GERAIS + PERGUNTAS_POR_PAPEL[papel]},
        "perguntas": {c: p for c, p in
                      PERGUNTAS_GERAIS + PERGUNTAS_POR_PAPEL[papel]},
        "achados_visuais": [],
        "o_que_a_peca_acerta": "",
    }
    (pacote / "revisao.json").write_text(
        json.dumps(form, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    vazou = [x for x in PROIBIDOS if (pacote / x).exists()]
    return {"pacote": str(pacote), "levados": levados, "faltando": faltando,
            "papel": papel, "vazou": vazou}


def pontua(d: Path) -> dict:
    d = d.resolve()
    form_p = d / "revisao" / "revisao.json"
    if not form_p.is_file():
        raise SystemExit(f"sem revisao: rode --preparar em {d}")
    form = json.loads(form_p.read_text(encoding="utf-8"))
    resp = form.get("respostas") or {}
    pendentes = [c for c, v in resp.items() if v is None]
    if pendentes:
        raise SystemExit("revisao incompleta, faltam: " + ", ".join(pendentes))

    # defeitos: le o lint que o lote ja rodou
    def carrega(nome):
        f = d / nome
        return json.loads(f.read_text(encoding="utf-8")) if f.is_file() else {}
    lc = carrega("lint_copy.json")
    le = carrega("lint_email.json")
    vs = (lc.get("violacoes") or []) + (le.get("violacoes") or [])
    b = [v for v in vs if v["severidade"] == "B"]
    a = [v for v in vs if v["severidade"] == "A"]
    m = [v for v in vs if v["severidade"] == "M"]

    gerais = [c for c, _ in PERGUNTAS_GERAIS]
    do_papel = [c for c, _ in PERGUNTAS_POR_PAPEL[form["papel"]]]
    sim_g = sum(1 for c in gerais if resp.get(c) is True)
    sim_p = sum(1 for c in do_papel if resp.get(c) is True)
    pq = [c for c in gerais + do_papel if resp.get(c) is False]

    motivos = []
    if b:
        nota = 3
        motivos += [f"{v['regra']} (B)" for v in b]
    else:
        nota = 10 - len(a) - min(2, 0.5 * len(m))
        motivos += [f"{v['regra']} (A)" for v in a]

    # o padrao de qualidade: nao basta nao errar
    teto = None
    if sim_g < 5 or sim_p < 3:
        teto = TETO_SEM_QUALIDADE
        motivos += [f"PQ:{c}" for c in pq]
    if teto is not None:
        nota = min(nota, teto)
    if pq and nota >= 10:
        nota = 9
    nota = max(0, int(round(nota)))

    ver_form = form.get("versao_catalogo")
    ver_hoje = _versao()
    out = {
        "nota": nota,
        "aprovada": nota >= NOTA_MINIMA and not b,
        "defeitos": {"B": len(b), "A": len(a), "M": len(m)},
        "qualidade": {"gerais": f"{sim_g}/6", "papel": f"{sim_p}/4",
                      "reprovadas": pq},
        "papel": form["papel"],
        "motivos": motivos,
        "versao_catalogo": ver_hoje,
        "versao_da_revisao": ver_form,
        "revisao_velha": ver_form != ver_hoje,
        "achados_visuais": form.get("achados_visuais") or [],
        "acerta": form.get("o_que_a_peca_acerta") or "",
    }
    (d / "veredito.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (d / "veredito.md").write_text(_veredito_md(out), encoding="utf-8")
    return out


def _veredito_md(o: dict) -> str:
    pq = "\n".join(f"  {c}" for c in o["qualidade"]["reprovadas"]) or "  nenhuma"
    av = "\n".join(f"  {x}" for x in o["achados_visuais"]) or "  nenhum"
    velha = ("\n> **Revisao velha.** Foi feita na versao "
             f"`{o['versao_da_revisao']}` e o catalogo esta em "
             f"`{o['versao_catalogo']}`. Refaca.\n"
             if o["revisao_velha"] else "")
    return f"""# Veredito

**NOTA: {o['nota']}/10** · {'aprovada' if o['aprovada'] else 'reprovada'}
{velha}
Defeitos: {o['defeitos']['B']} B · {o['defeitos']['A']} A · {o['defeitos']['M']} M
Padrao de qualidade: {o['qualidade']['gerais']} gerais · {o['qualidade']['papel']} do papel ({o['papel']})

## Padrao de qualidade reprovado

{pq}

## Achados visuais

{av}

## O que a peca acerta

{o['acerta'] or '  (nao preenchido)'}

---

Catalogo `{o['versao_catalogo']}`. Regra da nota em
`shared/postura-revisao.md`; as perguntas em `shared/padrao-de-qualidade.md`.
"""


def estado(d: Path) -> dict:
    d = Path(d).resolve()
    v = d / "veredito.json"
    if not v.is_file():
        return {"revisada": False, "motivo": "sem veredito.json"}
    o = json.loads(v.read_text(encoding="utf-8"))
    return {"revisada": True, "nota": o["nota"], "aprovada": o["aprovada"],
            "revisao_velha": o.get("revisao_velha", False),
            "versao": o.get("versao_catalogo")}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--preparar"), ap.add_argument("--pontuar")
    ap.add_argument("--estado"), ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    if a.preparar:
        r = preparar(Path(a.preparar))
        if a.json:
            print(json.dumps(r, ensure_ascii=False, indent=2))
        else:
            print(f"pacote: {r['pacote']}")
            print(f"papel:  {r['papel']}")
            print("levado: " + ", ".join(r["levados"]))
            if r["faltando"]:
                print("FALTA:  " + ", ".join(r["faltando"]))
            if r["vazou"]:
                print("VAZOU:  " + ", ".join(r["vazou"]))
            print("\nAgora: abra os PNGs, responda revisao.json, "
                  "e rode --pontuar.")
        return 1 if r["faltando"] or r["vazou"] else 0
    if a.pontuar:
        o = pontua(Path(a.pontuar))
        print(json.dumps(o, ensure_ascii=False, indent=2) if a.json
              else _veredito_md(o))
        return 0 if o["aprovada"] else 1
    if a.estado:
        print(json.dumps(estado(Path(a.estado)), ensure_ascii=False))
        return 0
    ap.print_help()
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
