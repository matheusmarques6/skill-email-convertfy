#!/usr/bin/env python3
"""Empacota cada skill em um zip para upload no claude.ai.

Um zip por skill em dist/. Cada zip tem a skill na raiz, no formato que o
claude.ai espera:

    <nome>/SKILL.md
    <nome>/references/*.md

As skills deste repo referenciam arquivos compartilhados (`shared/`,
`scripts/`) por caminho relativo a raiz do repo. Fora do repo esses
caminhos nao existem, entao o empacotador leva junto o que a skill
realmente cita, em `<nome>/shared/` e `<nome>/scripts/`, e reescreve os
caminhos dentro dos .md para apontar para a copia local.

Uso:
    python3 scripts/build_zip.py              # todas as skills
    python3 scripts/build_zip.py email-copy   # so uma
    python3 scripts/build_zip.py --lista      # so lista o que iria
"""

from __future__ import annotations

import re
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SKILLS = RAIZ / "skills"
DIST = RAIZ / "dist"

# Arquivos fora da pasta da skill que podem ser citados e devem viajar junto.
# Chave: caminho como aparece no markdown. Valor: caminho real no repo.
ANEXAVEIS = {
    "shared/anti-vicios-copy.md",
    "shared/anti-vicios-design.md",
    "shared/anti-vicios-processo.md",
    "shared/calibracao.md",
    "shared/postura-revisao.md",
    "shared/protocolo-de-execucao.md",
    "shared/vocabulario-arsenal.md",
    "shared/lexico/pt-br.txt",
    "shared/lexico/en.txt",
    "scripts/lint_copy.py",
    "scripts/lint_email.py",
    "marcas/_template.md",
}

# Citados com frequencia, mas grandes demais ou sem sentido fora do repo.
# Viram nota no README do zip em vez de arquivo.
SO_MENCAO = {
    "CLAUDE.md",
    "docs/pesquisa/pesquisa-vicios-ia-email.md",
    "docs/pesquisa/evidencias-publicadas.md",
    "docs/pesquisa/a-verificar.md",
    "docs/pesquisa/vault-vicios.md",
    "docs/indice-vault.md",
    "docs/destilacao/matriz.md",
}

RX_CAMINHO = re.compile(r"(?:\.\./)*((?:shared|scripts|marcas|docs)/[\w./-]+)")


def skills_disponiveis() -> list[str]:
    return sorted(p.name for p in SKILLS.iterdir() if (p / "SKILL.md").is_file())


def citados(pasta: Path) -> set[str]:
    """Caminhos anexaveis citados nos .md da skill."""
    achados: set[str] = set()
    for md in pasta.rglob("*.md"):
        for m in RX_CAMINHO.finditer(md.read_text(encoding="utf-8")):
            alvo = m.group(1)
            if alvo in ANEXAVEIS:
                achados.add(alvo)
    return achados


def reescreve(texto: str, anexados: set[str]) -> str:
    """Aponta os caminhos anexados para a copia local dentro do zip."""
    def troca(m: re.Match) -> str:
        alvo = m.group(1)
        return alvo if alvo in anexados else m.group(0)

    return RX_CAMINHO.sub(troca, texto)


def empacota(nome: str) -> Path:
    origem = SKILLS / nome
    if not (origem / "SKILL.md").is_file():
        raise SystemExit(f"skill sem SKILL.md: {nome}")

    anexados = citados(origem)
    DIST.mkdir(exist_ok=True)
    destino = DIST / f"{nome}.zip"

    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp) / nome
        base.mkdir()

        # a skill em si
        for arq in origem.rglob("*"):
            if not arq.is_file():
                continue
            rel = arq.relative_to(origem)
            saida = base / rel
            saida.parent.mkdir(parents=True, exist_ok=True)
            if arq.suffix == ".md":
                saida.write_text(
                    reescreve(arq.read_text(encoding="utf-8"), anexados),
                    encoding="utf-8",
                )
            else:
                shutil.copy2(arq, saida)

        # os compartilhados que ela cita
        for rel in sorted(anexados):
            fonte = RAIZ / rel
            if not fonte.is_file():
                print(f"  aviso: citado e ausente: {rel}")
                continue
            saida = base / rel
            saida.parent.mkdir(parents=True, exist_ok=True)
            if fonte.suffix == ".md":
                saida.write_text(
                    reescreve(fonte.read_text(encoding="utf-8"), anexados),
                    encoding="utf-8",
                )
            else:
                shutil.copy2(fonte, saida)

        (base / "LEIA-ME.md").write_text(_leia_me(nome, anexados), encoding="utf-8")

        with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
            for arq in sorted(base.rglob("*")):
                if arq.is_file():
                    z.write(arq, arq.relative_to(base.parent))

    return destino


def _leia_me(nome: str, anexados: set[str]) -> str:
    lista = "\n".join(f"- `{c}`" for c in sorted(anexados)) or "- (nenhum)"
    faltando = "\n".join(f"- `{c}`" for c in sorted(SO_MENCAO))
    return f"""# {nome}

Pacote gerado por `scripts/build_zip.py` a partir de
https://github.com/matheusmarques6/skill-email-convertfy

## O que veio junto

{lista}

## O que NAO veio, e a skill pode citar

Estes ficam no repo. Sem eles a skill funciona, mas perde rastreabilidade
e o gate de lint pode nao rodar:

{faltando}

Alem deles, `vault/` (fonte de verdade, somente leitura) e `vendor/`
(referencia externa) nunca entram no pacote.

## Licencas

Ver `NOTICE.md` e `LICENSES/` no repo. O Impeccable e Apache 2.0 e exige
NOTICE.
"""


def main(argv: list[str]) -> int:
    disponiveis = skills_disponiveis()
    args = [a for a in argv if not a.startswith("-")]

    if "--lista" in argv:
        for nome in disponiveis:
            print(f"{nome}  ->  dist/{nome}.zip  ({len(citados(SKILLS / nome))} anexos)")
        return 0

    alvos = args or disponiveis
    for nome in alvos:
        if nome not in disponiveis:
            print(f"skill desconhecida: {nome}")
            print(f"disponiveis: {', '.join(disponiveis)}")
            return 1

    for nome in alvos:
        caminho = empacota(nome)
        kb = caminho.stat().st_size / 1024
        print(f"{caminho.relative_to(RAIZ)}  ({kb:.1f} KB)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
