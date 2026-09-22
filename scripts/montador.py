#!/usr/bin/env python3
"""Monta a peca a partir do arsenal e do vault, sem copiar nada.

Regra do `assets/arsenal/README.md`: secao que tem variante no vault **nao**
vira arquivo aqui. Este montador respeita isso lendo o HTML do vault em
tempo de execucao, pelo symlink, e nunca guardando copia.

Ordem de montagem:

    casca-600
      header      arsenal (o vault tem zero variantes)
      hero        vault, se houver variante resolvida
      offer       oferta, cupom e prazo na primeira dobra
      cta         arsenal (o vault tem zero variantes)
      body        vault, ou paragrafos da copy
      products    vault, se houver variante resolvida
      rodape      fragmento
"""

from __future__ import annotations

import html as html_mod
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ARSENAL = RAIZ / "assets" / "arsenal"
VAULT_HTML = RAIZ / "vault" / "componentes" / "_html"


# O comentario de cabecalho de cada bloco documenta os slots, e por isso
# CONTEM os nomes dos slots. Se ele sobreviver ate a substituicao, o
# conteudo e injetado dentro do comentario e a peca renderiza quebrada:
# o `-->` do comentario fecha no meio do HTML. Tirar antes, nao depois.
RX_CABECALHO = re.compile(r"\A\s*<!--.*?-->\s*", re.S)


def bloco(caminho_rel: str) -> str:
    t = (ARSENAL / caminho_rel).read_text(encoding="utf-8")
    return RX_CABECALHO.sub("", t)


def preenche(tpl: str, slots: dict) -> str:
    for k, v in slots.items():
        tpl = tpl.replace(k, str(v))
    return tpl


def secao_do_vault(slug: str) -> str | None:
    """Le a secao do vault e devolve o miolo, sem <head> nem <body>.

    Le, nao copia: o arquivo continua so no vault. Se o slug nao existir,
    devolve None e quem chamou registra a lacuna, nunca inventa o bloco.
    """
    f = VAULT_HTML / f"{slug}.html"
    if not f.is_file():
        return None
    t = f.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"<body[^>]*>(.*)</body>", t, re.S | re.I)
    if not m:
        return None
    corpo = m.group(1)
    # NAO fatiar por <tr>: a regex nao-gulosa casa os <tr> aninhados das
    # tabelas internas e destroi o encaixe, o que faz a peca renderizar
    # duplicada e em cascata. O render pegou isso; o lint estatico nao.
    # A secao inteira entra dentro de UMA celula, preservando a estrutura
    # de tabela que o vault ja validou.
    corpo = re.sub(r"<!--.*?-->", "", corpo, flags=re.S)
    return ('<tr><td style="padding:0;background:#FFFFFF;">'
            + _adapta(corpo.strip()) + "</td></tr>")


# Placeholder neutro, como o design system da marca manda enquanto nao ha
# foto real. PNG cinza de 1 px em data URI: renderiza, nao quebra, e nao
# finge ser produto. SVG nao serve, e D18.
PLACEHOLDER_PNG = (
    "data:image/png;base64,"
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8Xw8AAoMBgDTD2qgAAAAASUVORK5CYII=")

# Qualquer src que seja um token em CAIXA_ALTA e slot nao preenchido, nao
# URL. Listar token por token nao escala: o vault tem 120 nomes diferentes.
RX_SRC_SLOT = re.compile(
    r'(src\s*=\s*)(["\'])\s*([A-Z][A-Z0-9]*(?:_[A-Z0-9]+)+)\s*\2')


def _adapta(miolo: str) -> str:
    """Ajusta o miolo do vault para conviver na casca de 600.

    O HTML do vault **nao e alterado**: a adaptacao acontece em memoria, a
    cada montagem.

    Duas coisas, e so duas:

    1. `src` que aponta para um slot nao preenchido vira placeholder neutro,
       para o render nao acusar imagem quebrada (R06). O design system da
       marca ja manda placeholder neutro enquanto nao ha foto real.
    2. A largura nao e reescrita aqui. Mexer em `width=` da variante gera
       atributo `style` duplicado e quebra o layout. Quem contem a largura e
       o CSS da casca, que vale para tudo que estiver dentro dela.
    """
    return RX_SRC_SLOT.sub(lambda m: f'{m.group(1)}{m.group(2)}{PLACEHOLDER_PNG}{m.group(2)}',
                           miolo)


def monta(copy: dict, ficha: dict, variantes: dict | None = None) -> dict:
    """Devolve {html, blocos_usados, lacunas}."""
    e = html_mod.escape
    variantes = variantes or {}
    cor = ficha.get("cor_primaria", "#111111")
    marca = (ficha.get("nome") or "LOJA").upper()
    usados, lacunas = [], []

    slots_base = {
        "NOME_DA_MARCA": e(marca),
        "COR_PRIMARIA": cor,
        "URL_DO_SITE_AQUI": "#",
        "URL_DO_CTA_AQUI": "#",
        "URL_DESCADASTRO": "#",
    }

    partes = []

    # header: arsenal, porque o vault tem zero variantes
    partes.append(preenche(bloco("blocos/header/header-1-wordmark-centralizado.html"),
                           slots_base))
    usados.append("arsenal:header-1-wordmark-centralizado")

    # hero: titulo da peca
    partes.append(
        f'<tr><td class="pad" style="padding:6px 24px 14px;background:#FFFFFF;'
        f'font-family:Helvetica,Arial,sans-serif;font-size:28px;line-height:1.2;'
        f'font-weight:bold;color:#111111;">{e(copy["assunto"])}</td></tr>')
    usados.append("hero:titulo-da-peca")

    # offer: primeira dobra, como a carteira manda
    oferta = copy.get("_oferta", "")
    if oferta:
        partes.append(
            f'<tr><td class="pad" style="padding:0 24px 16px;background:#FFFFFF;'
            f'font-family:Helvetica,Arial,sans-serif;font-size:17px;line-height:1.45;'
            f'font-weight:bold;color:{cor};">{e(oferta)}</td></tr>')
        usados.append("offer:linha-de-oferta")

    # cta: arsenal. com cupom quando o brief traz codigo
    cupom = copy.get("_cupom")
    prazo = copy.get("_prazo", "")
    if cupom:
        partes.append(preenche(bloco("blocos/cta/cta-2-botao-com-cupom.html"),
                               {**slots_base, "TEXTO_DO_CTA": e(copy["ctas"][0]),
                                "CODIGO_DO_CUPOM": e(cupom),
                                "PRAZO_DA_OFERTA": e(prazo)}))
        usados.append("arsenal:cta-2-botao-com-cupom")
    else:
        partes.append(preenche(bloco("blocos/cta/cta-1-botao-isolado.html"),
                               {**slots_base, "TEXTO_DO_CTA": e(copy["ctas"][0])}))
        usados.append("arsenal:cta-1-botao-isolado")

    # body: os paragrafos da copy
    for b in copy["blocos"]:
        partes.append(
            f'<tr><td class="pad" style="padding:0 24px 15px;background:#FFFFFF;'
            f'font-family:Helvetica,Arial,sans-serif;font-size:16px;line-height:1.55;'
            f'color:#1A1A1A;">{e(b)}</td></tr>')
    if copy["blocos"]:
        usados.append(f"body:{len(copy['blocos'])} paragrafos")

    # products: do vault, se o brief resolveu uma variante
    slug_prod = variantes.get("products")
    if slug_prod:
        miolo = secao_do_vault(slug_prod)
        if miolo:
            partes.append(miolo)
            usados.append(f"vault:{slug_prod}")
        else:
            lacunas.append(f"products: variante `{slug_prod}` nao tem HTML no vault")
    else:
        lacunas.append("products: nenhuma variante resolvida, a peca sai sem vitrine")

    # rodape
    partes.append(preenche(bloco("fragmentos/rodape-legal.html"),
                           {**slots_base,
                            "ENDERECO_FISICO": e(ficha.get("endereco", "[FALTA: endereco fisico do remetente]"))}))
    usados.append("fragmento:rodape-legal")

    casca = bloco("fragmentos/casca-600.html")
    pre = preenche(bloco("fragmentos/preheader.html"),
                   {"TEXTO_DE_PREHEADER_AQUI": e(copy.get("preheader", ""))})
    html = (casca.replace("LANG", copy.get("idioma", "pt-br"))
                 .replace("TITULO", e(copy["assunto"]))
                 .replace("PREHEADER", pre)
                 .replace("BLOCOS", "\n".join(partes)))
    return {"html": html, "blocos_usados": usados, "lacunas": lacunas}
