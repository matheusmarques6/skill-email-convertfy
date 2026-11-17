#!/usr/bin/env python3
"""lint_email.py: linter deterministico do HTML final de e-mail (Convertfy).

Implementa a secao 9.2 de docs/pesquisa/pesquisa-vicios-ia-email.md.
Python 3.11, apenas biblioteca padrao (html.parser, sem bs4).

Entrada: HTML (arquivo, argumento posicional, ou stdin).
Opcional: --marca ficha.json com as cores autorizadas da loja, no formato
{"cores": ["#1A1A1A", "#4F46E5"]}. Sem ficha, a peca e julgada como neutra
(fundo branco, texto preto), que e a regra fixa da Convertfy.

Saida JSON: mesmo contrato do lint_copy.py.

    {"ok", "bloqueia", "total", "violacoes": [{regra,severidade,campo,trecho,sugestao}]}

Exit code: 1 se houver qualquer violacao B, 0 caso contrario.

Severidade adotada (a coluna "status em e-mail" da secao 6 da pesquisa):
  B  D18 (recursos que quebram), tamanho acima de 102 KB, placeholder repetido
  A  status "Vicio" (D01 a D05, D17) e as faltas estruturais
  M  status "Revisar" e o que depende de contexto
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from html.parser import HTMLParser

SEVERIDADE = {
    "D01": "A", "D02": "B", "D03": "A", "D04": "A", "D05": "A",
    "D17": "A", "D17_SEM_LARGURA": "M", "D18": "B",
    "E_TAMANHO": "B", "E_CONTAINER": "A", "E_CONTAINER_LEGADO": "M",
    "E_PREHEADER": "A",
    "E_CTA_IMAGEM": "A", "E_PLACEHOLDER": "B",
    # Regra do vault (docs/pesquisa/vault-vicios.md), detectavel aqui.
    "V02": "B",
    # D21 a D31 entram como `revisar` (docs/decisoes.md, D-003): avisam em M,
    # nunca bloqueiam. Ver skills/email-design/references/tipografia.md.
    "D21": "M", "D26": "M", "D27": "M", "D28": "M", "D29": "M",
}
# D26: corpo abaixo de 14px; rodape abaixo de 11px. Rotulo curto (selo,
# legenda de preco) pode ter 12-13px: so conta como corpo a partir de
# PALAVRAS_DE_CORPO palavras.
PISO_CORPO_PX = 14
PISO_RODAPE_PX = 11
PALAVRAS_DE_CORPO = 7
# D21: imagem a partir desta largura, fora de link, rouba o clique no Gmail.
LARGURA_IMAGEM_GRANDE = 300
ALTURA_FAIXA_DECORATIVA = 150
LIMITE_CLIPPING = 102 * 1024
CONTAINER_PADRAO = 600
# 598 e legado aceito: avisa em M e NAO manda regerar peca que ja existe.
CONTAINER_LEGADO = 598
CONTAINERS_OK = {CONTAINER_LEGADO, CONTAINER_PADRAO}

CORES_NOMEADAS = {
    "white": (255, 255, 255), "black": (0, 0, 0), "red": (255, 0, 0),
    "green": (0, 128, 0), "blue": (0, 0, 255), "gray": (128, 128, 128),
    "grey": (128, 128, 128), "silver": (192, 192, 192), "navy": (0, 0, 128),
    "beige": (245, 245, 220), "ivory": (255, 255, 240), "transparent": None,
    "inherit": None, "none": None,
}


# ---------------------------------------------------------------------------
# Cor
# ---------------------------------------------------------------------------
def parse_cor(valor: str):
    if not valor:
        return None
    v = valor.strip().lower()
    if v in CORES_NOMEADAS:
        return CORES_NOMEADAS[v]
    m = re.fullmatch(r"#([0-9a-f]{3}|[0-9a-f]{6})", v)
    if m:
        h = m.group(1)
        if len(h) == 3:
            h = "".join(c * 2 for c in h)
        return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))
    m = re.match(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)", v)
    if m:
        return (int(m.group(1)), int(m.group(2)), int(m.group(3)))
    return None


def hexa(rgb) -> str:
    return "#%02X%02X%02X" % rgb


def luminancia(rgb) -> float:
    def canal(c):
        c = c / 255.0
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = rgb
    return 0.2126 * canal(r) + 0.7152 * canal(g) + 0.0722 * canal(b)


def contraste(a, b) -> float:
    la, lb = luminancia(a), luminancia(b)
    claro, escuro = max(la, lb), min(la, lb)
    return (claro + 0.05) / (escuro + 0.05)


def hsl(rgb):
    r, g, b = [c / 255.0 for c in rgb]
    mx, mn = max(r, g, b), min(r, g, b)
    lum = (mx + mn) / 2
    if mx == mn:
        return 0.0, 0.0, lum
    d = mx - mn
    sat = d / (2 - mx - mn) if lum > 0.5 else d / (mx + mn)
    if mx == r:
        h = ((g - b) / d) % 6
    elif mx == g:
        h = (b - r) / d + 2
    else:
        h = (r - g) / d + 4
    return h * 60, sat, lum


def e_violeta(rgb) -> bool:
    h, s, _l = hsl(rgb)
    return 240 <= h <= 295 and s >= 0.20


def e_bege(rgb) -> bool:
    h, s, l = hsl(rgb)
    return 20 <= h <= 60 and 0.05 <= s <= 0.60 and l >= 0.85


# ---------------------------------------------------------------------------
# Parser
# ---------------------------------------------------------------------------
def parse_style(valor: str) -> dict:
    out = {}
    for par in (valor or "").split(";"):
        if ":" in par:
            k, v = par.split(":", 1)
            out[k.strip().lower()] = v.strip()
    return out


def largura_de(attrs: dict) -> int | None:
    bruto = attrs.get("width")
    if bruto:
        m = re.match(r"\s*(\d+)", str(bruto))
        if m:
            return int(m.group(1))
    style = parse_style(attrs.get("style", ""))
    for chave in ("width", "max-width"):
        if chave in style:
            m = re.match(r"\s*(\d+)", style[chave])
            if m:
                return int(m.group(1))
    return None


def tamanho_px(valor: str) -> float | None:
    """font-size em px. Aceita px e pt (pt * 4/3). em, rem e % voltam None:
    sem a base, o lint nao chuta."""
    m = re.match(r"\s*(\d+(?:\.\d+)?)\s*(px|pt)?\s*(!important)?\s*$",
                 valor or "", re.IGNORECASE)
    if not m:
        return None
    n = float(m.group(1))
    return n * 4 / 3 if (m.group(2) or "").lower() == "pt" else n


GENERICAS = {"sans-serif", "serif", "monospace", "cursive", "fantasy",
             "system-ui", "-apple-system", "inherit", "initial"}


def primeira_familia(valor: str) -> str | None:
    """Primeira familia de uma pilha font-family, normalizada. A pilha
    'Montserrat, Helvetica, Arial' conta como Montserrat: e a familia que o
    designer escolheu, o resto e fallback."""
    for parte in (valor or "").split(","):
        nome = parte.strip().strip("'\"").strip().lower()
        nome = re.sub(r"\s*!important$", "", nome)
        if nome and nome not in GENERICAS:
            # Arial e Helvetica sao a mesma escolha (a fallback segura); nao
            # contam como duas familias. Idem Georgia e Times.
            return FAMILIA_SEGURA.get(nome, nome)
    return None


FAMILIA_SEGURA = {
    "arial": "sans segura", "helvetica": "sans segura",
    "helvetica neue": "sans segura", "arial nova": "sans segura",
    "georgia": "serif segura", "times new roman": "serif segura",
    "times": "serif segura",
}


RX_DESCADASTRO = re.compile(
    r"unsubscribe|descadastr|cancelar\s+inscri|darse\s+de\s+baja|abmelden"
    r"|desinscri",
    re.IGNORECASE,
)


OCULTO = re.compile(
    r"(display\s*:\s*none|max-height\s*:\s*0|font-size\s*:\s*0|opacity\s*:\s*0"
    r"|mso-hide\s*:\s*all)",
    re.IGNORECASE,
)


class LeitorEmail(HTMLParser):
    """Coleta o que o lint precisa: textos com cor e fundo, imagens, links."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.pilha = []            # [(tag, cor, fundo, oculto)]
        self.textos = []           # (texto, cor, fundo, oculto)
        self.imagens = []          # dict de atributos
        self.links = []            # dict: texto, tem_img, fundo
        self.larguras_container = []
        self.tem_svg = False
        self._link_atual = None
        # Camada de tipografia (D26, D28): pilha paralela a `pilha`, com o
        # tamanho de fonte herdado e o td mais interno de cada elemento.
        self.pilha_tipo = []       # [(px, id_td)]
        self.tipos = []            # dict: texto, px, td, apos_descadastro, oculto
        self.familias = []         # primeira familia de cada font-family inline
        self.botoes = []           # dict: fundo, texto (a com padding)
        self._td_seq = 0
        self._viu_descadastro = False
        self.tds_descadastro = set()

    # -- estado ------------------------------------------------------------
    def _herda(self):
        if self.pilha:
            _t, cor, fundo, oculto = self.pilha[-1]
            return cor, fundo, oculto
        return None, (255, 255, 255), False

    def handle_starttag(self, tag, attrs):
        a = {k.lower(): (v or "") for k, v in attrs}
        style = parse_style(a.get("style", ""))
        cor_pai, fundo_pai, oculto_pai = self._herda()
        cor = parse_cor(style.get("color", "")) or cor_pai
        atalho = (style.get("background", "") or "").split()
        fundo = (
            parse_cor(style.get("background-color", ""))
            or parse_cor(atalho[0] if atalho else "")
            or parse_cor(a.get("bgcolor", ""))
            or fundo_pai
        )
        oculto = oculto_pai or bool(OCULTO.search(a.get("style", ""))) or (
            "preheader" in (a.get("class", "") + a.get("id", "")).lower()
        )
        px_pai, td_pai = self.pilha_tipo[-1] if self.pilha_tipo else (None, None)
        px = tamanho_px(style.get("font-size", "")) or px_pai
        td = td_pai
        if tag == "td":
            self._td_seq += 1
            td = self._td_seq
        familia = primeira_familia(style.get("font-family", ""))
        if familia:
            self.familias.append(familia)
        if tag not in ("img", "br", "hr", "meta", "link", "input", "source"):
            self.pilha.append((tag, cor, fundo, oculto))
            self.pilha_tipo.append((px, td))

        if tag == "svg":
            self.tem_svg = True
        if tag == "img":
            a["_largura"] = largura_de(a)
            a["_linkada"] = self._link_atual is not None
            self.imagens.append(a)
            if self._link_atual is not None:
                self._link_atual["tem_img"] = True
        if tag == "table" or tag == "td":
            w = largura_de(a)
            if w and w >= 300:
                self.larguras_container.append(w)
        if tag == "a":
            href = a.get("href", "")
            self._link_atual = {"texto": "", "tem_img": False, "fundo": fundo,
                                "href": href}
            self.links.append(self._link_atual)
            if RX_DESCADASTRO.search(href):
                self._marca_descadastro(td)
            if "padding" in style and not oculto:
                self.botoes.append({"fundo": fundo, "link": self._link_atual})

    def _marca_descadastro(self, td):
        self._viu_descadastro = True
        if td is not None:
            self.tds_descadastro.add(td)

    def handle_endtag(self, tag):
        if tag == "a":
            self._link_atual = None
        for i in range(len(self.pilha) - 1, -1, -1):
            if self.pilha[i][0] == tag:
                del self.pilha[i:]
                del self.pilha_tipo[i:]
                break

    def handle_data(self, data):
        if not data.strip():
            return
        cor, fundo, oculto = self._herda()
        self.textos.append((data.strip(), cor, fundo, oculto))
        px, td = self.pilha_tipo[-1] if self.pilha_tipo else (None, None)
        if self._link_atual is not None:
            self._link_atual["texto"] += data
            if RX_DESCADASTRO.search(data):
                self._marca_descadastro(td)
        self.tipos.append({
            "texto": data.strip(), "px": px, "td": td, "oculto": oculto,
            "apos_descadastro": self._viu_descadastro,
        })


# ---------------------------------------------------------------------------
# Achados
# ---------------------------------------------------------------------------
def achado(regra, campo, trecho, sugestao):
    return {
        "regra": regra.split("_")[0] if regra.startswith("D17_") else regra,
        "severidade": SEVERIDADE.get(regra, "M"),
        "campo": campo,
        "trecho": str(trecho).strip()[:160],
        "sugestao": sugestao,
    }


# ---------------------------------------------------------------------------
# Regras
# ---------------------------------------------------------------------------
RX_POSITION_ABS = re.compile(r"position\s*:\s*absolute", re.IGNORECASE)
RX_TRANSFORM = re.compile(r"(^|[;\s\"'{])transform\s*:", re.IGNORECASE)
RX_FONT_FACE = re.compile(r"@font-face", re.IGNORECASE)
RX_IMG_TAG = re.compile(r"<img\b[^>]*>", re.IGNORECASE)
RX_BORDER_RADIUS = re.compile(r"border-radius", re.IGNORECASE)
RX_FONT_FAMILY_FALLBACK = re.compile(
    r"font-family\s*:[^;\"'}]*,[^;\"'}]*", re.IGNORECASE
)


def regra_d18(html: str, leitor: LeitorEmail):
    out = []
    if RX_POSITION_ABS.search(html):
        out.append(achado("D18", "html", "position: absolute",
                          "Outlook ignora posicionamento absoluto: use tabela"))
    if RX_TRANSFORM.search(html):
        out.append(achado("D18", "html", "transform:",
                          "transform nao renderiza em Outlook: remova"))
    for tag in RX_IMG_TAG.findall(html):
        if RX_BORDER_RADIUS.search(tag):
            out.append(achado("D18", "img", tag[:120],
                              "border-radius em img vira quadrado no Outlook: "
                              "use imagem ja recortada"))
            break
    if leitor.tem_svg:
        out.append(achado("D18", "html", "<svg",
                          "SVG inline nao renderiza na maioria dos clientes: use PNG"))
    if RX_FONT_FACE.search(html) and not RX_FONT_FAMILY_FALLBACK.search(html):
        out.append(achado("D18", "html", "@font-face",
                          "webfont sem pilha de fallback: declare "
                          "font-family com Helvetica, Arial, sans-serif"))
    return out


def regra_d17(leitor: LeitorEmail):
    out = []
    for img in leitor.imagens:
        alt = img.get("alt")
        largura = img.get("_largura")
        if alt is None or not alt.strip():
            src = img.get("src", "")[:80]
            if largura is not None and largura > 200:
                out.append(achado("D17", "img", src or "(sem src)",
                                  "imagem principal precisa de alt descritivo com "
                                  "a oferta"))
            elif largura is None:
                out.append(achado("D17_SEM_LARGURA", "img", src or "(sem src)",
                                  "imagem sem largura declarada e sem alt: declare "
                                  "width e alt"))
    return out


def regra_contraste(leitor: LeitorEmail):
    out = []
    vistos = set()
    for texto, cor, fundo, oculto in leitor.textos:
        if oculto or cor is None or fundo is None:
            continue
        razao = contraste(cor, fundo)
        if razao < 4.5:
            chave = (hexa(cor), hexa(fundo))
            if chave in vistos:
                continue
            vistos.add(chave)
            regra = "D05" if fundo != (255, 255, 255) else "D04"
            out.append(
                achado(
                    regra,
                    "texto",
                    f"{texto[:60]} ({hexa(cor)} sobre {hexa(fundo)}, "
                    f"{razao:.2f}:1)",
                    "contraste minimo 4,5:1. Corpo em #000 ou #1A1A1A; sobre cor, "
                    "use branco ou preto",
                )
            )
    return out


def regra_tamanho(html: str):
    n = len(html.encode("utf-8"))
    if n > LIMITE_CLIPPING:
        return [
            achado(
                "E_TAMANHO",
                "html",
                f"{n} bytes",
                "acima do corte do Gmail (cerca de 102 KB, valor a reconfirmar em "
                "docs/pesquisa/a-verificar.md): o descadastro pode ficar abaixo do "
                "corte",
            )
        ]
    return []


def regra_container(leitor: LeitorEmail):
    if not leitor.larguras_container:
        return [
            achado(
                "E_CONTAINER",
                "html",
                "(nenhuma largura de container encontrada)",
                "declare o container de 600px com width=600",
            )
        ]
    if CONTAINER_PADRAO in leitor.larguras_container:
        return []
    if CONTAINER_LEGADO in leitor.larguras_container:
        return [
            achado(
                "E_CONTAINER_LEGADO",
                "html",
                f"container de {CONTAINER_LEGADO}px",
                "legado aceito: 600 e o padrao para peca nova, mas nao regere "
                "peca que ja existe so por causa disto",
            )
        ]
    achados = sorted(set(leitor.larguras_container))
    return [
        achado(
            "E_CONTAINER",
            "html",
            ", ".join(str(w) for w in achados),
            f"container da Convertfy e {CONTAINER_PADRAO}px",
        )
    ]


def regra_preheader(leitor: LeitorEmail):
    for _texto, _cor, _fundo, oculto in leitor.textos:
        if oculto:
            return []
    return [
        achado(
            "E_PREHEADER",
            "html",
            "",
            "sem preheader: inclua um bloco oculto com a condicao da oferta em texto",
        )
    ]


def regra_cta_imagem(leitor: LeitorEmail):
    if not leitor.links:
        return []
    com_texto = [l for l in leitor.links if l["texto"].strip()]
    so_imagem = [l for l in leitor.links if l["tem_img"] and not l["texto"].strip()]
    if so_imagem and not com_texto:
        return [
            achado(
                "E_CTA_IMAGEM",
                "a",
                so_imagem[0].get("href", "")[:80],
                "CTA so em imagem: repita a acao em texto vivo (botao bulletproof "
                "com texto)",
            )
        ]
    return []


RX_PLACEHOLDER = re.compile(r"\[[^\]\[<>]{2,60}\]")
RX_LOREM = re.compile(r"lorem ipsum", re.IGNORECASE)


def regra_placeholder(leitor: LeitorEmail):
    out = []
    contagem = {}
    for texto, _c, _f, _o in leitor.textos:
        if RX_LOREM.search(texto):
            out.append(achado("E_PLACEHOLDER", "texto", texto[:60],
                              "lorem ipsum na peca final"))
            break
    for texto, _c, _f, _o in leitor.textos:
        for m in RX_PLACEHOLDER.finditer(texto):
            chave = m.group(0).strip().lower()
            contagem[chave] = contagem.get(chave, 0) + 1
    for chave, n in contagem.items():
        if n >= 2:
            out.append(
                achado(
                    "E_PLACEHOLDER",
                    "texto",
                    f"{chave} x{n}",
                    "placeholder repetido identico: o agente truncou a peca, "
                    "preencha bloco a bloco",
                )
            )
        elif chave.startswith("[falta"):
            out.append(
                achado("E_PLACEHOLDER", "texto", chave,
                       "lacuna declarada nao preenchida: peca o dado ao cliente")
            )
    return out


def regra_cores_marca(leitor: LeitorEmail, cores_marca: set):
    out = []
    vistos = set()
    for link in leitor.links:
        fundo = link.get("fundo")
        if fundo and e_violeta(fundo) and hexa(fundo) not in cores_marca:
            if hexa(fundo) in vistos:
                continue
            vistos.add(hexa(fundo))
            out.append(
                achado(
                    "D01",
                    "a",
                    hexa(fundo),
                    "indigo ou violeta em botao sem constar na ficha da marca: "
                    "use a cor da marca ou preto",
                )
            )
    for _texto, _cor, fundo, _oculto in leitor.textos:
        if fundo and e_bege(fundo) and hexa(fundo) not in cores_marca:
            if hexa(fundo) in vistos:
                continue
            vistos.add(hexa(fundo))
            out.append(
                achado(
                    "D03",
                    "fundo",
                    hexa(fundo),
                    "fundo creme ou bege sem constar na ficha da marca: o padrao "
                    "Convertfy e fundo branco",
                )
            )
    return out


RX_GRADIENTE = re.compile(r"(linear-gradient|radial-gradient|backdrop-filter)",
                          re.IGNORECASE)


def regra_d02(html: str):
    m = RX_GRADIENTE.search(html)
    if m:
        return [
            achado(
                "D02",
                "html",
                m.group(0),
                "gradiente, glow e glassmorphism nao renderizam em Outlook e "
                "marcam IA: use cor chapada",
            )
        ]
    return []



# ---------------------------------------------------------------------------
# V02  Incentivo existindo so dentro da imagem
# ---------------------------------------------------------------------------
# Com imagens bloqueadas, ou no resumidor de IA, o codigo e o prazo somem.
# Nao basta ter alt: o alt precisa carregar o incentivo.
RX_INCENTIVO = re.compile(
    r"\d{1,3}\s*%"                      # 20%
    r"|R\$\s*\d"                        # R$30
    r"|\b[A-Z][A-Z0-9]{4,}\b"            # BEMVINDO10
    r"|\bfrete\s+gr[aá]tis\b"
    r"|\bfree\s+shipping\b",
    re.IGNORECASE,
)


def regra_v02(leitor: LeitorEmail):
    tem_imagem_grande = any(
        (img.get("_largura") or 0) >= 200 for img in leitor.imagens
    )
    if not tem_imagem_grande:
        return []

    # Texto vivo e o que o cliente le com imagens bloqueadas: fora do
    # preheader oculto, que nao aparece no corpo.
    vivo = " ".join(t for t, _cor, _fundo, oculto in leitor.textos if not oculto)
    if RX_INCENTIVO.search(vivo):
        return []

    no_alt = any(RX_INCENTIVO.search(img.get("alt") or "") for img in leitor.imagens)
    sugestao = (
        "o incentivo precisa existir fora da imagem: uma linha de texto vivo "
        "com valor, codigo e prazo"
        if no_alt else
        "o incentivo so existe dentro da imagem: nem o texto vivo nem o alt "
        "carregam valor, codigo ou prazo"
    )
    return [achado("V02", "html", "(nenhum incentivo em texto vivo)", sugestao)]


# ---------------------------------------------------------------------------
# Camada visual: D21, D26, D27, D28, D29 (status `revisar`, severidade M)
# ---------------------------------------------------------------------------
# Catalogadas em shared/anti-vicios-design.md desde a destilacao, sem
# checagem em codigo ate aqui. Regra dura so em prosa e o que o vault
# proibe; estas sao as partes que o HTML prova sozinho.

def regra_d21(leitor: LeitorEmail):
    """Imagem grande fora de link: o Gmail abre no lightbox e o toque nao
    vai para a loja."""
    soltas = []
    for img in leitor.imagens:
        largura = img.get("_largura") or 0
        m = re.match(r"\s*(\d+)", str(img.get("height") or ""))
        altura = int(m.group(1)) if m else None
        # Faixa decorativa baixa (divisor, transicao de 70px) nao abre
        # lightbox: e o espacador da regra, nao imagem grande.
        if altura is not None and altura < ALTURA_FAIXA_DECORATIVA:
            continue
        if largura >= LARGURA_IMAGEM_GRANDE and not img.get("_linkada"):
            soltas.append(img.get("src", "")[:60] or "(sem src)")
    if not soltas:
        return []
    return [achado(
        "D21", "img", f"{soltas[0]} ({len(soltas)} imagem(ns))",
        "imagem grande sem link: envolva em <a> com o mesmo destino do CTA "
        "(a hero) ou do produto (foto de produto)")]


def _e_rodape(t: dict, leitor: LeitorEmail) -> bool:
    return t["apos_descadastro"] or (t["td"] in leitor.tds_descadastro)


def regra_d26(leitor: LeitorEmail):
    """Fonte pequena para caber copy: corte a copy, nao a fonte."""
    corpo, rodape = [], []
    for t in leitor.tipos:
        if t["oculto"] or t["px"] is None:
            continue
        if _e_rodape(t, leitor):
            if t["px"] < PISO_RODAPE_PX:
                rodape.append(t)
        elif t["px"] < PISO_CORPO_PX and len(t["texto"].split()) >= PALAVRAS_DE_CORPO:
            corpo.append(t)
        elif t["px"] < PISO_RODAPE_PX:
            corpo.append(t)
    out = []
    if corpo:
        t = corpo[0]
        out.append(achado(
            "D26", "texto",
            f"{t['texto'][:50]} ({t['px']:g}px; {len(corpo)} trecho(s))",
            f"corpo com piso de {PISO_CORPO_PX}px (16 preferido). Se nao cabe, "
            "a secao esta cheia: corte a copy, nao a fonte"))
    if rodape:
        t = rodape[0]
        out.append(achado(
            "D26", "rodape",
            f"{t['texto'][:50]} ({t['px']:g}px)",
            f"rodape com piso de {PISO_RODAPE_PX}px"))
    return out


RX_TEXT_SHADOW = re.compile(r"text-shadow\s*:", re.IGNORECASE)


def regra_d27(html: str):
    m = RX_TEXT_SHADOW.search(html)
    if not m:
        return []
    return [achado("D27", "html", "text-shadow",
                   "sombra em texto some ou borra em varios clientes: "
                   "resolva legibilidade com contraste e fundo chapado")]


def regra_d28(leitor: LeitorEmail):
    """Tres ou mais familias. Conta a primeira familia de cada pilha."""
    vistas = []
    for f in leitor.familias:
        if f not in vistas:
            vistas.append(f)
    if len(vistas) >= 3:
        return [achado("D28", "font-family", ", ".join(vistas[:5]),
                       "no maximo duas familias: a tipografia principal e a "
                       "fonte secundaria da ficha")]
    return []


def regra_d29(leitor: LeitorEmail):
    """Duas cores de botao principal. Botao = <a> com padding e fundo de cor.
    Fundo branco ou quase branco e botao fantasma (secundario): nao conta."""
    cores = []
    for b in leitor.botoes:
        fundo = b["fundo"]
        if fundo is None or luminancia(fundo) > 0.85:
            continue
        hx = hexa(fundo)
        if hx not in cores:
            cores.append(hx)
    if len(cores) >= 2:
        return [achado("D29", "a", ", ".join(cores),
                       "uma cor de CTA na peca inteira: o segundo botao vira "
                       "link de texto ou botao fantasma")]
    return []


# ---------------------------------------------------------------------------
# Execucao
# ---------------------------------------------------------------------------
ORDEM_SEV = {"B": 0, "A": 1, "M": 2}



def _versao_catalogo() -> str:
    """Carimba a versao das regras na saida, para medicao antiga nao passar
    por atual. Falha silenciosa e proposital: o lint nao deve quebrar porque
    o carimbo nao foi calculado."""
    try:
        import importlib.util
        _p = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          "versao_catalogo.py")
        _s = importlib.util.spec_from_file_location("versao_catalogo", _p)
        _m = importlib.util.module_from_spec(_s)
        _s.loader.exec_module(_m)
        return _m.versao()
    except Exception:
        return "cat-desconhecida"


def lint(html: str, cores_marca=None) -> dict:
    cores_marca = {c.upper() for c in (cores_marca or [])}
    leitor = LeitorEmail()
    leitor.feed(html)
    leitor.close()

    violacoes = []
    violacoes += regra_d18(html, leitor)
    violacoes += regra_d02(html)
    violacoes += regra_d17(leitor)
    violacoes += regra_contraste(leitor)
    violacoes += regra_tamanho(html)
    violacoes += regra_container(leitor)
    violacoes += regra_preheader(leitor)
    violacoes += regra_cta_imagem(leitor)
    violacoes += regra_placeholder(leitor)
    violacoes += regra_cores_marca(leitor, cores_marca)
    violacoes += regra_v02(leitor)
    violacoes += regra_d21(leitor)
    violacoes += regra_d26(leitor)
    violacoes += regra_d27(html)
    violacoes += regra_d28(leitor)
    violacoes += regra_d29(leitor)

    violacoes.sort(key=lambda v: (ORDEM_SEV[v["severidade"]], v["regra"]))
    bloqueia = any(v["severidade"] == "B" for v in violacoes)
    return {
        "versao_catalogo": _versao_catalogo(),
        "ok": not violacoes,
        "bloqueia": bloqueia,
        "total": len(violacoes),
        "violacoes": violacoes,
    }


def formata_texto(resultado: dict) -> str:
    if resultado["ok"]:
        return "lint_email: sem violacoes."
    linhas = []
    for v in resultado["violacoes"]:
        linhas.append(
            f"[{v['severidade']}] {v['regra']} {v['campo']}: {v['trecho']}\n"
            f"        -> {v['sugestao']}"
        )
    linhas.append(
        f"\n{resultado['total']} violacoes. "
        + ("ENTREGA BLOQUEADA (severidade B)." if resultado["bloqueia"] else "Nenhuma B.")
    )
    return "\n".join(linhas)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Linter de HTML de e-mail (Convertfy)")
    ap.add_argument("arquivo", nargs="?", help="HTML de entrada (default: stdin)")
    ap.add_argument("--json", action="store_true", help="saida em JSON")
    ap.add_argument("--marca", help="ficha JSON da marca com as cores autorizadas")
    args = ap.parse_args(argv)

    html = (
        open(args.arquivo, "r", encoding="utf-8").read()
        if args.arquivo and args.arquivo != "-"
        else sys.stdin.read()
    )
    cores = []
    if args.marca and os.path.exists(args.marca):
        with open(args.marca, "r", encoding="utf-8") as fh:
            ficha = json.load(fh)
        cores = ficha.get("cores") or []
    resultado = lint(html, cores)
    if args.json:
        print(json.dumps(resultado, ensure_ascii=False, indent=2))
    else:
        print(formata_texto(resultado))
    return 1 if resultado["bloqueia"] else 0


if __name__ == "__main__":
    sys.exit(main())
