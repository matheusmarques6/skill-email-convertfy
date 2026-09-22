#!/usr/bin/env python3
"""Converte uma nota de variante do contrato legado para o contrato novo.

O contrato NOVO e o canonico. As 43 notas legadas continuam no vault como
estao (o vault e somente leitura daqui) e sao convertidas em memoria, no
momento em que uma delas e escolhida.

O que a conversao faz:

  carrega    os 14 campos que os dois contratos compartilham
  deriva     `profundidade` a partir de `aliviador`
  aposenta   `momento`, `momento_vetado`, `ativa`, `densidade_no_banco`,
             `serve_estruturas`, `diretivas_de_imagem`
  nao deriva `aliviador`, que e julgamento e precisa de decisao humana

`aliviador` vem de `shared/aliviador-legado.json`, que e o registro das
decisoes ja tomadas. Slug ausente do registro sai como nao resolvido, e a
skill NAO pode gerar com ele: peca a decisao.

Uso:
    python3 scripts/adaptar_variante_legado.py <slug|caminho>
    python3 scripts/adaptar_variante_legado.py --todas --relatorio
    python3 scripts/adaptar_variante_legado.py <slug> --json
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
VARIANTES = RAIZ / "vault" / "componentes" / "variantes"
REGISTRO = RAIZ / "shared" / "aliviador-legado.json"

# Campos que os dois contratos tem. Passam sem alteracao.
COMPARTILHADOS = [
    "tipo", "slug", "secao", "nome_no_banco", "variant_id", "status", "fonte",
    "schema_campos", "product_slots", "itens", "objecao", "registro",
    "registro_vetado", "paleta", "papel_na_peca", "peso", "convivencia",
    "exige", "aprendizados", "requisitos_de_reviews",
]

# So existem no legado. Nao entram no contrato novo.
APOSENTADOS = {
    "ativa": "substituido por `status`",
    "momento": "eixo aposentado no contrato novo",
    "momento_vetado": "eixo aposentado no contrato novo",
    "densidade_no_banco": "nao consta no contrato novo",
    "serve_estruturas": "nao consta no contrato novo",
    "diretivas_de_imagem": "vira brief de imagem, nao campo de contrato",
}

# Observado nas 32 notas do contrato novo. `transparencia_de_politica` e o
# unico ambiguo (aparece com `garantia` e com `afirmacao`), entao nao deriva.
ALIVIADOR_PARA_PROFUNDIDADE = {
    "dado_de_adequacao": "afirmacao",
    "demonstracao_de_mecanismo": "mecanismo",
    "comparacao_de_categoria": "mecanismo",
    "prova_de_terceiro": "prova_de_terceiro",
    "prova_por_volume": "prova_de_terceiro",
    # transparencia_de_politica: ambiguo de proposito, ver docstring
}

NAO_RESOLVIDO = "[FALTA: decisao humana]"


def frontmatter(texto: str) -> str:
    """O bloco entre os dois `---` de nivel de linha.

    Nao use split('---'): o frontmatter legado tem comentarios do tipo
    `# --- eixos de ranking ---`, que truncariam o bloco no meio.
    """
    linhas = texto.splitlines()
    if not linhas or linhas[0].strip() != "---":
        return ""
    for i in range(1, len(linhas)):
        if linhas[i].strip() == "---":
            return "\n".join(linhas[1:i])
    return ""


def campos(fm: str) -> dict[str, str]:
    saida: dict[str, str] = {}
    for linha in fm.splitlines():
        if linha.lstrip().startswith("#") or not linha.strip():
            continue
        m = re.match(r"^([a-z_]+):\s*(.*)$", linha)
        if m:
            saida[m.group(1)] = m.group(2).strip()
    return saida


def e_legado(c: dict[str, str]) -> bool:
    return "aliviador" not in c


def registro_aliviador() -> dict[str, str]:
    if not REGISTRO.is_file():
        return {}
    dados = json.loads(REGISTRO.read_text(encoding="utf-8"))
    return {k: v for k, v in dados.items() if not k.startswith("_")}


def acha_nota(alvo: str) -> Path:
    p = Path(alvo)
    if p.is_file():
        return p
    achados = list(VARIANTES.rglob(f"{alvo}.md"))
    if not achados:
        raise SystemExit(f"variante nao encontrada: {alvo}")
    if len(achados) > 1:
        raise SystemExit(
            f"slug ambiguo: {alvo}\n  " + "\n  ".join(str(a) for a in achados)
        )
    return achados[0]


def adapta(caminho: Path, reg: dict[str, str] | None = None) -> dict:
    reg = registro_aliviador() if reg is None else reg
    c = campos(frontmatter(caminho.read_text(encoding="utf-8")))
    slug = c.get("slug", caminho.stem)

    if not e_legado(c):
        return {
            "slug": slug, "contrato": "novo", "convertido": False,
            "pronto": True, "campos": c, "aposentados": {}, "pendencias": [],
        }

    novo = {k: c[k] for k in COMPARTILHADOS if k in c}
    novo["contrato"] = "legado"
    pendencias: list[str] = []

    aliviador = reg.get(slug)
    if aliviador:
        valores = [v.strip() for v in aliviador.strip("[]").split(",") if v.strip()]
        novo["aliviador"] = "[" + ", ".join(valores) + "]"
        prof = ALIVIADOR_PARA_PROFUNDIDADE.get(valores[0]) if valores else None
        if prof:
            novo["profundidade"] = prof
        else:
            novo["profundidade"] = NAO_RESOLVIDO
            pendencias.append(
                f"profundidade nao deriva de `{valores[0] if valores else '?'}`"
            )
    else:
        novo["aliviador"] = NAO_RESOLVIDO
        novo["profundidade"] = NAO_RESOLVIDO
        pendencias.append("aliviador nao registrado em shared/aliviador-legado.json")

    aposentados = {k: APOSENTADOS[k] for k in APOSENTADOS if k in c}

    return {
        "slug": slug, "contrato": "legado", "convertido": True,
        "pronto": not pendencias, "campos": novo,
        "aposentados": aposentados, "pendencias": pendencias,
    }


def imprime(r: dict) -> None:
    print(f"# {r['slug']}  ({r['contrato']})")
    if not r["convertido"]:
        print("  ja esta no contrato novo, nada a fazer")
        return
    print("\n---")
    for k, v in r["campos"].items():
        print(f"{k}: {v}")
    print("---")
    if r["aposentados"]:
        print("\n# aposentados na conversao")
        for k, motivo in r["aposentados"].items():
            print(f"#   {k}: {motivo}")
    if r["pendencias"]:
        print("\n# PENDENCIAS, nao gere com esta variante:")
        for p in r["pendencias"]:
            print(f"#   {p}")


def relatorio() -> int:
    reg = registro_aliviador()
    legadas, prontas = [], 0
    for p in sorted(VARIANTES.rglob("*.md")):
        r = adapta(p, reg)
        if r["contrato"] != "legado":
            continue
        legadas.append(r)
        prontas += bool(r["pronto"])
    print(f"legadas: {len(legadas)}  prontas: {prontas}  "
          f"pendentes: {len(legadas) - prontas}\n")
    for r in legadas:
        marca = "ok  " if r["pronto"] else "FALTA"
        print(f"  {marca} {r['slug']}")
        for p in r["pendencias"]:
            print(f"        {p}")
    return 0 if prontas == len(legadas) else 1


def main(argv: list[str]) -> int:
    if "--relatorio" in argv or "--todas" in argv:
        return relatorio()
    alvos = [a for a in argv if not a.startswith("-")]
    if not alvos:
        print(__doc__)
        return 2
    reg = registro_aliviador()
    saidas = [adapta(acha_nota(a), reg) for a in alvos]
    if "--json" in argv:
        print(json.dumps(saidas, ensure_ascii=False, indent=2))
    else:
        for r in saidas:
            imprime(r)
    return 0 if all(r["pronto"] for r in saidas) else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
