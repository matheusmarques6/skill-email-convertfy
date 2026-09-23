#!/usr/bin/env python3
"""Versao do catalogo de regras, derivada do conteudo.

Versao escrita a mao desatualiza sem ninguem perceber. Esta e calculada a
partir dos arquivos que definem regra: muda o lexico ou uma regra do lint,
muda a versao, sem ninguem lembrar de incrementar.

Aconteceu de verdade: o `lint_status` do vault foi de 2 limpas para 1
depois que V29, V36 e V52 entraram, e o texto continuou dizendo 2. Com a
versao carimbada, a medicao antiga fica visivelmente velha.

Uso:
    python3 scripts/versao_catalogo.py          # a versao
    python3 scripts/versao_catalogo.py --json   # com a composicao
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

# Arquivos que definem regra. Mudou aqui, mudou o veredito de alguma peca.
FONTES = [
    "scripts/lint_copy.py",
    "scripts/lint_email.py",
    "shared/lexico/pt-br.txt",
    "shared/lexico/en.txt",
    "shared/anti-vicios-copy.md",
    "shared/anti-vicios-design.md",
    "shared/anti-vicios-processo.md",
    "shared/anti-vicios-visuais.md",
    "shared/calibracao.md",
    "shared/padrao-de-qualidade.md",
]


def _ids(texto: str) -> set[str]:
    return set(re.findall(r"\b(?:C\d{2}|D\d{2}|P\d{2}|R\d{2}|V\d{2}|PQ\d+|E_[A-Z_]+)\b",
                          texto))


def calcula() -> dict:
    h = hashlib.sha256()
    ids: set[str] = set()
    presentes, ausentes = [], []
    for rel in FONTES:
        f = RAIZ / rel
        if not f.is_file():
            ausentes.append(rel)
            continue
        b = f.read_bytes()
        h.update(rel.encode())
        h.update(b)
        ids |= _ids(b.decode("utf-8", "replace"))
        presentes.append(rel)
    curto = h.hexdigest()[:8]
    return {
        "versao": f"cat-{curto}",
        "regras_distintas": len(ids),
        "fontes": presentes,
        "fontes_ausentes": ausentes,
        "familias": {p: sum(1 for i in ids if i.startswith(p))
                     for p in ("C", "D", "P", "R", "V", "E_")},
    }


def versao() -> str:
    return calcula()["versao"]


if __name__ == "__main__":
    d = calcula()
    if "--json" in sys.argv:
        print(json.dumps(d, ensure_ascii=False, indent=2))
    else:
        print(d["versao"])
