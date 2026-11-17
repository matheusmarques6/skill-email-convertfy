#!/usr/bin/env python3
"""Monta a vitrine dos modulos de e-commerce e passa no lint.

Os trechos de HTML de `skills/email-design/references/modulos-ecommerce.md`
sao referencia de construcao. Trecho de referencia que ninguem roda apodrece
calado: este script extrai cada bloco marcado com

    ```html modulo=<slug>

troca os slots por valores de exemplo, monta tudo na `casca-600` do arsenal
e roda o `lint_email.py`. Com --render, gera tambem os tres PNGs do ciclo.

Saidas em `evals/render/vitrine-modulos/` (fora do git, regeravel):

    vitrine.html      a peca montada
    img/*.png         imagens de exemplo geradas aqui (sem rede)
    lint.json         o resultado do lint
    desktop-600.png, mobile-375.png, dark-600.png  (com --render)

Uso:
    python3 scripts/vitrine_modulos.py            # monta e roda o lint
    python3 scripts/vitrine_modulos.py --render   # e renderiza
    python3 scripts/vitrine_modulos.py --listar   # so lista os modulos

Exit code: 1 se algum slot ficou sem valor ou se o lint achou qualquer
violacao. A vitrine e o caso bom: nem M passa.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
REFERENCIA = RAIZ / "skills" / "email-design" / "references" / "modulos-ecommerce.md"
CASCA = RAIZ / "assets" / "arsenal" / "fragmentos" / "casca-600.html"
PREHEADER = RAIZ / "assets" / "arsenal" / "fragmentos" / "preheader.html"
RODAPE_LEGAL = RAIZ / "assets" / "arsenal" / "fragmentos" / "rodape-legal.html"
SAIDA = RAIZ / "evals" / "render" / "vitrine-modulos"

RX_MODULO = re.compile(r"^```html modulo=([a-z0-9-]+)\s*\n(.*?)^```\s*$",
                       re.MULTILINE | re.DOTALL)
# Slot: palavra em caixa alta com sublinhado (o padrao do arsenal).
RX_SLOT = re.compile(r"\b[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)+\b")
RX_COMENTARIO = re.compile(r"<!--(?!\[if|<!\[endif).*?-->", re.DOTALL)

LOJA = "https://loja.exemplo.com.br"

# Imagens geradas localmente: (largura, altura, cor de fundo, rotulo).
IMAGENS = {
    "logo": (280, 72, (255, 255, 255), "LOJA EXEMPLO"),
    "hero": (1200, 900, (214, 205, 196), "hero 4:3"),
    "fundo": (1200, 880, (40, 40, 44), "fundo escuro"),
    "produto": (1080, 1080, (230, 230, 228), "produto 1:1"),
    "p1": (520, 520, (226, 222, 216), "1:1"),
    "p2": (520, 520, (210, 216, 222), "1:1"),
    "p3": (520, 520, (222, 214, 222), "1:1"),
    "p4": (520, 520, (216, 222, 210), "1:1"),
    "linha": (360, 360, (224, 224, 224), "1:1"),
    "contagem": (880, 220, (17, 17, 17), "02 : 14 : 37 : 09"),
}

VALORES = {
    # gerais
    "COR_DO_BOTAO": "#111111",
    "URL_DO_SITE": LOJA,
    "URL_DO_LOGO": "img/logo.png",
    "NOME_DA_MARCA": "Loja Exemplo",
    "URL_DO_CTA": f"{LOJA}/colecoes/inverno",
    "TEXTO_DO_CTA": "VER A COLEÇÃO",
    # hero
    "URL_DA_IMAGEM_HERO": "img/hero.png",
    "ALT_DO_HERO": "Casaco de lã cinza em modelo, 20% OFF até domingo",
    "HEADLINE_DO_HERO": "O casaco que esgotou em maio voltou",
    "PROPOSTA_DE_VALOR": "20% OFF com o cupom INVERNO20 até domingo, 23h59.",
    "URL_DA_IMAGEM_DE_FUNDO": "img/fundo.png",
    # oferta
    "ROTULO_DA_OFERTA": "SÓ ATÉ DOMINGO",
    "VALOR_DA_OFERTA": "20% OFF",
    "CONDICAO_DA_OFERTA": "Em toda a coleção de inverno, sem valor mínimo.",
    "CODIGO_DO_CUPOM": "INVERNO20",
    "PRAZO_DA_OFERTA": "Válido até domingo, 23h59.",
    # botao e link
    "URL_DA_COLECAO": f"{LOJA}/colecoes/todas",
    "TEXTO_DO_LINK_SECUNDARIO": "Ver todos os produtos",
    # produto
    "URL_DO_PRODUTO": f"{LOJA}/produtos/casaco-la",
    "URL_FOTO_PRODUTO": "img/produto.png",
    "ALT_DO_PRODUTO": "Casaco de lã cinza, vista de frente",
    "NOME_DO_PRODUTO": "Casaco de lã cinza",
    "PRECO_DE": "R$ 489,90",
    "PRECO_POR": "R$ 391,92",
    "BENEFICIO_EM_UMA_FRASE": "Lã batida que não pinica, com forro até o punho.",
    "TEXTO_DO_CTA_PRODUTO": "COMPRAR O CASACO",
    "DETALHE_DO_PRODUTO": "Tamanho M, cor grafite",
    "TEXTO_DO_LINK_PRODUTO": "COMPRAR",
    # grade
    "URL_PRODUTO_1": f"{LOJA}/produtos/1", "URL_PRODUTO_2": f"{LOJA}/produtos/2",
    "URL_FOTO_1": "img/p1.png", "URL_FOTO_2": "img/p2.png",
    "ALT_PRODUTO_1": "Suéter de tricô cru", "ALT_PRODUTO_2": "Calça de sarja azul",
    "NOME_PRODUTO_1": "Suéter de tricô cru", "NOME_PRODUTO_2": "Calça de sarja azul",
    "PRECO_DE_1": "R$ 259,90", "PRECO_DE_2": "R$ 219,90",
    "PRECO_POR_1": "R$ 207,92", "PRECO_POR_2": "R$ 175,92",
    # avaliacao
    "NOTA_MEDIA": "4,8",
    "NUMERO_DE_AVALIACOES": "1.284",
    "TRECHO_DA_AVALIACAO": "Comprei o cinza e voltei pra pegar o preto. "
                           "Esquenta sem pesar.",
    "NOME_DO_CLIENTE": "Marina T.",
    "SELO_DA_AVALIACAO": "Compra verificada",
    # garantias
    "GARANTIA_1": "Frete grátis acima de R$ 299",
    "GARANTIA_2": "Troca grátis em 30 dias",
    "GARANTIA_3": "Até 6x sem juros",
    # texto de pessoa
    "SAUDACAO_COM_NOME": "Oi, Ana.",
    "PARAGRAFO_1": "Separei o casaco que você olhou semana passada. Ele "
                   "esgotou em maio e voltou ontem, nas mesmas três cores.",
    "PARAGRAFO_2": "O cupom INVERNO20 vale até domingo, e dá para trocar em "
                   "30 dias se não servir.",
    "LINK_DE_ACAO": "Ver o casaco",
    "NOME_DE_QUEM_ASSINA": "Júlia Prado",
    "CARGO_E_LOJA": "Atendimento, Loja Exemplo",
    # contagem
    "URL_DO_GIF_DE_CONTAGEM": "img/contagem.png",
    "PRAZO_POR_EXTENSO": "domingo, 23h59",
    # rodape
    "URL_CATEGORIA_1": f"{LOJA}/c/novidades", "CATEGORIA_1": "NOVIDADES",
    "URL_CATEGORIA_2": f"{LOJA}/c/casacos", "CATEGORIA_2": "CASACOS",
    "URL_CATEGORIA_3": f"{LOJA}/c/tricos", "CATEGORIA_3": "TRICÔS",
    "URL_CATEGORIA_4": f"{LOJA}/c/sale", "CATEGORIA_4": "SALE",
    # fragmentos do arsenal
    "URL_DESCADASTRO": "{{unsubscribe_url}}",
    "ENDERECO_FISICO": "Rua Exemplo 100, São Paulo, SP, 01000-000",
    "TEXTO_DE_PREHEADER_AQUI": "20% OFF em toda a coleção de inverno com o "
                               "cupom INVERNO20, até domingo.",
}


def modulos(texto: str | None = None) -> list[tuple[str, str]]:
    texto = texto if texto is not None else REFERENCIA.read_text(encoding="utf-8")
    return [(m.group(1), m.group(2)) for m in RX_MODULO.finditer(texto)]


RX_LINHA_SLOTS = re.compile(r"^Slots:(.*?)(?:\n\n|\Z)", re.MULTILINE | re.DOTALL)
RX_SLOT_DECLARADO = re.compile(r"`([A-Z][A-Z0-9_]*)`")


def slots_problematicos(texto: str | None = None) -> list[str]:
    """Slot declarado na linha 'Slots:' que o RX_SLOT nao reconhece.

    Aconteceu: `SAUDACAO`, sem sublinhado, passou pela troca e saiu cru na
    vitrine. Todo slot precisa de ao menos um sublinhado."""
    texto = texto if texto is not None else REFERENCIA.read_text(encoding="utf-8")
    ruins = []
    for m in RX_LINHA_SLOTS.finditer(texto):
        for slot in RX_SLOT_DECLARADO.findall(m.group(1)):
            if not RX_SLOT.fullmatch(slot):
                ruins.append(slot)
    return ruins


def sem_comentario_de_doc(html: str) -> str:
    """Tira comentario de documentacao, preserva os condicionais do Outlook."""
    return RX_COMENTARIO.sub("", html)


def preenche(html: str, valores: dict) -> tuple[str, set[str]]:
    faltando = set()

    def troca(m):
        slot = m.group(0)
        if slot in valores:
            return valores[slot]
        faltando.add(slot)
        return slot

    return RX_SLOT.sub(troca, html), faltando


def monta(lista=None) -> tuple[str, set[str]]:
    lista = lista if lista is not None else modulos()
    blocos = []
    for slug, html in lista:
        blocos.append(f"<!-- modulo: {slug} -->\n{html.strip()}")
    rodape = sem_comentario_de_doc(RODAPE_LEGAL.read_text(encoding="utf-8"))
    blocos.append(rodape.strip())
    casca = sem_comentario_de_doc(CASCA.read_text(encoding="utf-8"))
    pre = sem_comentario_de_doc(PREHEADER.read_text(encoding="utf-8")).strip()
    peca = (casca.replace("LANG", "pt-BR")
                 .replace("TITULO", "Vitrine de modulos")
                 .replace("PREHEADER", pre)
                 .replace("BLOCOS", "\n".join(blocos)))
    return preenche(peca, VALORES)


def gera_imagens(destino: Path):
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        return False
    destino.mkdir(parents=True, exist_ok=True)
    for nome, (w, h, cor, rotulo) in IMAGENS.items():
        img = Image.new("RGB", (w, h), cor)
        d = ImageDraw.Draw(img)
        claro = sum(cor) > 380
        tinta = (60, 60, 60) if claro else (235, 235, 235)
        d.text((w // 2, h // 2), rotulo, fill=tinta, anchor="mm")
        img.save(destino / f"{nome}.png")
    return True


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--render", action="store_true", help="gera os 3 PNGs")
    ap.add_argument("--listar", action="store_true", help="so lista os modulos")
    args = ap.parse_args(argv)

    lista = modulos()
    if args.listar:
        for slug, _ in lista:
            print(slug)
        return 0

    sys.path.insert(0, str(RAIZ / "scripts"))
    import lint_email  # noqa: E402

    html, faltando = monta(lista)
    SAIDA.mkdir(parents=True, exist_ok=True)
    (SAIDA / "vitrine.html").write_text(html, encoding="utf-8")
    gera_imagens(SAIDA / "img")

    r = lint_email.lint(html)
    (SAIDA / "lint.json").write_text(
        json.dumps(r, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"{len(lista)} modulos montados em {SAIDA / 'vitrine.html'}")
    ruins = slots_problematicos()
    if ruins:
        print("slots sem sublinhado (nao sao trocados): " + ", ".join(ruins))
        faltando = set(faltando) | set(ruins)
    if faltando:
        print("slots sem valor de exemplo: " + ", ".join(sorted(faltando)))
    print(lint_email.formata_texto(r))

    if args.render:
        import render  # noqa: E402
        rel = render.renderiza(SAIDA / "vitrine.html", nome="vitrine-modulos",
                               saida=SAIDA)
        print(f"render: {rel.get('altura_px')} px no desktop, "
              f"{rel.get('peso_kb')} KB")

    return 1 if (faltando or not r["ok"]) else 0


if __name__ == "__main__":
    sys.exit(main())
