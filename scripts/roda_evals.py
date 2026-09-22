#!/usr/bin/env python3
"""Roda os linters contra evals/ruins/ e mede a taxa de deteccao.

Cada caso declara em `_manifesto.json` se e detectavel por lint ou se
depende do revisor. A taxa e reportada separada, de proposito: misturar
os dois produz um numero que parece bom e nao significa nada.

Uso:
    python3 scripts/roda_evals.py
    python3 scripts/roda_evals.py --json
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
RUINS = RAIZ / "evals" / "ruins"


def roda_lint(caso: dict) -> set[str]:
    arq = RUINS / caso["arquivo"]
    script = "lint_copy.py" if caso["tipo"] == "copy" else "lint_email.py"
    r = subprocess.run(
        [sys.executable, str(RAIZ / "scripts" / script), "--json", str(arq)],
        capture_output=True, text=True,
    )
    if not r.stdout.strip():
        return set()
    try:
        d = json.loads(r.stdout)
    except json.JSONDecodeError:
        return set()
    return {v["regra"] for v in d.get("violacoes", [])}


def main(argv: list[str]) -> int:
    manifesto = json.loads((RUINS / "_manifesto.json").read_text(encoding="utf-8"))
    linhas = []
    for caso in manifesto:
        achadas = roda_lint(caso)
        esperada = caso["regra_esperada"]
        # Regra V nao existe no lint: o que vale e o lint ter pegado ALGO.
        pegou_exata = esperada in achadas
        pegou_algo = bool(achadas)
        linhas.append({**caso, "achadas": sorted(achadas),
                       "pegou_exata": pegou_exata, "pegou_algo": pegou_algo})

    de_lint = [l for l in linhas if l["deteccao"] == "lint"]
    de_revisor = [l for l in linhas if l["deteccao"] == "revisor"]
    ok_lint = sum(1 for l in de_lint if l["pegou_exata"])
    algo_revisor = sum(1 for l in de_revisor if l["pegou_algo"])

    if "--json" in argv:
        print(json.dumps({"casos": linhas,
                          "lint": {"total": len(de_lint), "detectados": ok_lint},
                          "revisor": {"total": len(de_revisor),
                                      "pegos_por_tabela": algo_revisor}},
                         ensure_ascii=False, indent=2))
        return 0 if ok_lint == len(de_lint) else 1

    largura = max(len(l["id"]) for l in linhas) + 2
    print("CASOS DETECTAVEIS POR LINT")
    print("-" * 64)
    for l in de_lint:
        marca = "ok  " if l["pegou_exata"] else "FALHA"
        extra = "" if l["pegou_exata"] else f"  (achou: {', '.join(l['achadas']) or 'nada'})"
        print(f"  {marca} {l['id']:<{largura}} espera {l['regra_esperada']}{extra}")

    print("\nCASOS QUE DEPENDEM DO REVISOR")
    print("-" * 64)
    print("  Regra de posicao, sequencia ou verdade externa. O lint nao")
    print("  alcanca, e isso e projeto, nao defeito.")
    for l in de_revisor:
        colateral = f"  lint pegou de tabela: {', '.join(l['achadas'])}" if l["achadas"] else ""
        print(f"  --   {l['id']:<{largura}} espera {l['regra_esperada']}{colateral}")

    pct = 100 * ok_lint / len(de_lint) if de_lint else 0
    print("\n" + "=" * 64)
    print(f"  Deteccao do lint:  {ok_lint}/{len(de_lint)}  ({pct:.0f}%)")
    print(f"  Fora do lint:      {len(de_revisor)} casos, para o revisor")
    print(f"  Destes, o lint pegou algo de tabela em {algo_revisor}")
    print(f"  Total de casos:    {len(linhas)}")
    print("=" * 64)
    return 0 if ok_lint == len(de_lint) else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
