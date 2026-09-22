#!/usr/bin/env python3
"""lint_copy.py: linter deterministico de copy de e-mail (Convertfy).

Implementa a secao 9.1 de docs/pesquisa/pesquisa-vicios-ia-email.md.
Python 3.11, apenas biblioteca padrao. Le os lexicos de shared/lexico/.

Entrada: JSON (arquivo, argumento posicional, ou stdin).

    {
      "idioma": "pt-BR",              # "pt-BR" | "en" (default: pt-BR)
      "tipo": "campanha",             # welcome | campanha | carrinho | editorial
      "assunto": "...",
      "preheader": "...",
      "blocos": ["..."],              # ou [{"texto": "...", "papel": "body"}]
      "ctas": ["Comprar agora"],      # ou [{"texto": "...", "url": "..."}]
      "alts": ["..."],
      "brief_numbers": ["17", "100"], # numeros que existem no brief da loja
      "marca_usa_emoji": false
    }

Saida JSON:

    {
      "ok": bool,          # nenhuma violacao
      "bloqueia": bool,    # existe ao menos uma violacao de severidade B
      "total": int,
      "violacoes": [{"regra","severidade","campo","trecho","sugestao"}]
    }

Exit code: 1 se houver qualquer violacao B, 0 caso contrario.

Nota de calibracao: e-mail tem 40 a 150 palavras (secao 4.2 da pesquisa), entao
limiar por mil palavras nao funciona. Todos os limiares aqui sao contagem
absoluta por e-mail.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import sys
import unicodedata

# ---------------------------------------------------------------------------
# Severidade por regra. B bloqueia entrega, A corrige antes de enviar,
# M e aceitavel se isolado.
# ---------------------------------------------------------------------------
SEVERIDADE = {
    "C01": "B", "C02": "B", "C03": "B", "C04": "B", "C05": "B", "C07": "B",
    "C10": "A", "C11": "A", "C12": "A", "C13": "M", "C14": "M", "C15": "M",
    "C16": "A", "C17": "M", "C18": "M",
    "C20": "A", "C21": "A", "C22": "A", "C23": "A", "C24": "M", "C25": "M",
    "C26": "A",
    "C30": "M", "C31": "M", "C32": "M", "C33": "M", "C34": "M", "C35": "M",
    "C40": "M", "C40_GRAVE": "A", "C41": "A", "C42": "A", "C43": "M",
    "C44": "M", "C45": "A", "C46": "A", "C47": "A",
}

LEXICO_DIR_PADRAO = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "shared", "lexico"
)

# ---------------------------------------------------------------------------
# Dobra de acentos preservando o indice 1 para 1 (para reportar o trecho certo)
# ---------------------------------------------------------------------------
_ACENTOS = {}
for _base in "aeiouncyAEIOUNCY":
    for _comb in "̧̀́̂̃̈̊":
        _comp = unicodedata.normalize("NFC", _base + _comb)
        if len(_comp) == 1:
            _ACENTOS[ord(_comp)] = _base.lower()
_TABELA_DOBRA = dict(_ACENTOS)
_TABELA_DOBRA[ord("ç")] = "c"
_TABELA_DOBRA[ord("Ç")] = "c"


def dobra(texto: str) -> str:
    """Minuscula e sem acento, com o mesmo comprimento do original."""
    return texto.translate(_TABELA_DOBRA).lower()


# ---------------------------------------------------------------------------
# Lexico
# ---------------------------------------------------------------------------
class Entrada:
    __slots__ = ("regra", "padrao", "sugestao", "modo", "rx")

    def __init__(self, regra, padrao, sugestao, modo):
        self.regra = regra
        self.padrao = padrao
        self.sugestao = sugestao
        self.modo = modo
        self.rx = compila_padrao(padrao)


def compila_padrao(padrao: str) -> re.Pattern:
    if padrao.startswith("re:"):
        return re.compile(padrao[3:], re.IGNORECASE | re.UNICODE)
    if padrao.endswith("*"):
        radical = dobra(padrao[:-1])
        return re.compile(r"\b" + re.escape(radical) + r"[a-z]{0,3}\b")
    literal = dobra(padrao)
    return re.compile(r"(?<!\w)" + re.escape(literal) + r"(?!\w)")


def carrega_lexico(caminho: str) -> list[Entrada]:
    entradas = []
    with open(caminho, "r", encoding="utf-8") as fh:
        for n, linha in enumerate(fh, 1):
            linha = linha.rstrip("\n")
            if not linha.strip() or linha.lstrip().startswith("#"):
                continue
            campos = linha.split("|")
            if len(campos) < 2:
                raise ValueError(f"{caminho}:{n}: linha sem padrao")
            regra = campos[0].strip().upper()
            # Os campos sao lidos das pontas para o meio, para que o padrao
            # possa conter | (alternancia de regex).
            modo = "unitario"
            if len(campos) >= 4 and campos[-1].strip() in ("unitario", "densidade"):
                modo = campos[-1].strip()
                sugestao = campos[-2].strip()
                padrao = "|".join(campos[1:-2]).strip()
            elif len(campos) >= 3:
                sugestao = campos[-1].strip()
                padrao = "|".join(campos[1:-1]).strip()
            else:
                sugestao = ""
                padrao = "|".join(campos[1:]).strip()
            if not padrao:
                raise ValueError(f"{caminho}:{n}: padrao vazio")
            entradas.append(Entrada(regra, padrao, sugestao, modo))
    return entradas


def arquivo_lexico(idioma: str, lexico_dir: str) -> str:
    nome = "pt-br.txt" if idioma == "pt-br" else "en.txt"
    return os.path.join(lexico_dir, nome)


# ---------------------------------------------------------------------------
# Normalizacao da entrada
# ---------------------------------------------------------------------------
def normaliza_idioma(valor) -> str:
    v = (valor or "pt-BR").strip().lower().replace("_", "-")
    return "pt-br" if v.startswith("pt") else "en"


def como_texto(item) -> str:
    if isinstance(item, dict):
        for chave in ("texto", "text", "conteudo", "value"):
            if chave in item and item[chave]:
                return str(item[chave])
        return ""
    return "" if item is None else str(item)


class Peca:
    """Campos da peca em formato uniforme."""

    def __init__(self, dados: dict):
        self.idioma = normaliza_idioma(dados.get("idioma"))
        self.tipo = (dados.get("tipo") or "campanha").strip().lower()
        self.assunto = como_texto(dados.get("assunto"))
        self.preheader = como_texto(dados.get("preheader"))
        self.blocos = [como_texto(b) for b in (dados.get("blocos") or [])]
        self.blocos = [b for b in self.blocos if b.strip()]
        brutos_cta = dados.get("ctas") or []
        self.ctas = [como_texto(c) for c in brutos_cta]
        self.cta_urls = [
            (c.get("url") or c.get("href") or "") if isinstance(c, dict) else ""
            for c in brutos_cta
        ]
        self.alts = [como_texto(a) for a in (dados.get("alts") or [])]
        self.brief_numbers = [
            str(n) for n in (dados.get("brief_numbers") or [])
        ]
        self.marca_usa_emoji = bool(dados.get("marca_usa_emoji"))

    def campos(self):
        """(nome do campo, texto) para todo texto visivel da peca."""
        saida = []
        if self.assunto:
            saida.append(("assunto", self.assunto))
        if self.preheader:
            saida.append(("preheader", self.preheader))
        for i, b in enumerate(self.blocos):
            saida.append((f"blocos[{i}]", b))
        for i, c in enumerate(self.ctas):
            if c.strip():
                saida.append((f"ctas[{i}]", c))
        for i, a in enumerate(self.alts):
            if a.strip():
                saida.append((f"alts[{i}]", a))
        return saida

    def campos_de_prosa(self):
        """Somente o que e frase: assunto, preheader e blocos."""
        return [
            (nome, texto)
            for nome, texto in self.campos()
            if not nome.startswith("ctas[") and not nome.startswith("alts[")
        ]


# ---------------------------------------------------------------------------
# Achados
# ---------------------------------------------------------------------------
def achado(regra, campo, trecho, sugestao, severidade=None):
    sev = severidade or SEVERIDADE.get(regra, "M")
    return {
        "regra": regra.replace("_GRAVE", ""),
        "severidade": sev,
        "campo": campo,
        "trecho": trecho.strip()[:160],
        "sugestao": sugestao,
    }


def recorta(texto: str, inicio: int, fim: int, janela: int = 40) -> str:
    a = max(0, inicio - janela)
    b = min(len(texto), fim + janela)
    return ("..." if a > 0 else "") + texto[a:b] + ("..." if b < len(texto) else "")


# ---------------------------------------------------------------------------
# C01  Travessao
# ---------------------------------------------------------------------------
RX_TRAVESSAO = re.compile("[—–]")


def regra_c01(peca):
    out = []
    for campo, texto in peca.campos():
        for m in RX_TRAVESSAO.finditer(texto):
            out.append(
                achado(
                    "C01",
                    campo,
                    recorta(texto, m.start(), m.end()),
                    "troque por virgula, dois pontos, ponto ou parenteses",
                )
            )
    return out


# ---------------------------------------------------------------------------
# C02  Numero orfao (sem origem no brief)
# ---------------------------------------------------------------------------
RX_NUMERO = re.compile(r"(?<![\w#])(\d[\d.,]*)(?!\w)")
RX_MOEDA_ANTES = re.compile(r"(R\$|US\$|\$|€|£)\s*$")


def _digitos(s: str) -> str:
    return re.sub(r"\D", "", s)


def regra_c02(peca):
    permitidos = {_digitos(n) for n in peca.brief_numbers if _digitos(n)}
    out = []
    for campo, texto in peca.campos():
        for m in RX_NUMERO.finditer(texto):
            bruto = m.group(1).rstrip(".,")
            if not bruto:
                continue
            depois = texto[m.end(): m.end() + 2]
            antes = texto[: m.start()]
            if depois.lstrip().startswith("%"):
                continue  # percentual da oferta
            if RX_MOEDA_ANTES.search(antes):
                continue  # preco da oferta
            if _digitos(bruto) in permitidos:
                continue
            out.append(
                achado(
                    "C02",
                    campo,
                    recorta(texto, m.start(), m.end()),
                    f"numero {bruto} nao esta em brief_numbers: use dado real da "
                    f"loja ou corte",
                )
            )
    return out


# ---------------------------------------------------------------------------
# C03  Assunto que simula transacao
# ---------------------------------------------------------------------------
RX_C03 = [
    re.compile(r"^\s*\(?\s*(re|fw|fwd|enc|res)\s*\)?\s*:", re.IGNORECASE),
    re.compile(
        r"pedido\s+(foi\s+|esta\s+|est\u00e1\s+)?"
        r"(aprovado|confirmado|revisado|enviado|recebido|processado|atualizado)",
        re.IGNORECASE,
    ),
    re.compile(r"^\s*aviso\s*:", re.IGNORECASE),
    # Simetrico ao pt-BR: "was" e "is" contam tanto quanto "has been". Sem
    # isso, "Your order was approved" passava em loja inglesa, e C03 e B.
    re.compile(
        r"your\s+order\s+(has\s+been\s+|was\s+|is\s+)?"
        r"(approved|confirmed|shipped|reviewed|processed|received|updated)",
        re.IGNORECASE,
    ),
    re.compile(r"^\s*(notice|alert)\s*:", re.IGNORECASE),
]


def regra_c03(peca):
    out = []
    if not peca.assunto:
        return out
    for rx in RX_C03:
        m = rx.search(peca.assunto)
        if m:
            out.append(
                achado(
                    "C03",
                    "assunto",
                    peca.assunto,
                    "assunto de campanha nao pode simular transacao: diga a oferta",
                )
            )
            break
    return out


# ---------------------------------------------------------------------------
# C04  Idioma errado (cupom e CTA)
# ---------------------------------------------------------------------------
PALAVRAS_CUPOM = {
    "pt-br": ["PEDIDO", "COMPRA", "DESCONTO", "BEMVINDO", "BOASVINDAS", "FRETE",
              "PRIMEIRA", "PRIMEIRO", "OFERTA", "CUPOM", "GANHE", "VOLTE"],
    "en": ["ORDER", "WELCOME", "SAVE", "SHIP", "FIRST", "DEAL", "SALE", "FREE",
           "EXTRA", "GIFT"],
}
VERBOS_CTA = {
    "pt-br": ["comprar", "ver", "aproveitar", "garantir", "resgatar", "escolher",
              "pedir", "conferir", "ativar", "usar", "comecar", "quero", "baixar",
              "descobrir", "explorar", "montar"],
    "en": ["shop", "claim", "explore", "start", "add", "save", "discover", "find",
           "get", "buy", "view", "use", "redeem", "browse", "see", "apply"],
}
RX_TOKEN_CUPOM = re.compile(r"\b[A-Z][A-Z0-9]{3,19}\b")


def regra_c04(peca):
    outro = "en" if peca.idioma == "pt-br" else "pt-br"
    estrangeiras = PALAVRAS_CUPOM[outro]
    out = []
    for campo, texto in peca.campos():
        for m in RX_TOKEN_CUPOM.finditer(texto):
            token = m.group(0)
            for palavra in estrangeiras:
                if palavra in token:
                    out.append(
                        achado(
                            "C04",
                            campo,
                            token,
                            f"cupom precisa estar no idioma da loja ({peca.idioma})",
                        )
                    )
                    break
    verbos_estrangeiros = set(VERBOS_CTA[outro])
    verbos_da_loja = set(VERBOS_CTA[peca.idioma])
    for i, cta in enumerate(peca.ctas):
        if not cta.strip():
            continue
        primeira = dobra(cta.strip()).split()[0].strip(".,!:;")
        if primeira in verbos_estrangeiros and primeira not in verbos_da_loja:
            out.append(
                achado(
                    "C04",
                    f"ctas[{i}]",
                    cta,
                    f"CTA precisa estar no idioma da loja ({peca.idioma})",
                )
            )
    return out


# ---------------------------------------------------------------------------
# C05  Cena fabricada
# ---------------------------------------------------------------------------
RX_C05 = [
    re.compile(r"\bs[ãa]o \d{1,2} de [a-zà-ÿ]+", re.IGNORECASE),
    re.compile(r"\b\d{1,2}(:\d{2})?\s*(h|horas)?\s*da\s+(manh[ãa]|tarde|noite)\b",
               re.IGNORECASE),
    re.compile(r"\bestou escrevendo\b", re.IGNORECASE),
    re.compile(r"\bi'?m writing (this|to you)\b", re.IGNORECASE),
    re.compile(r"\bit'?s \d{1,2}(:\d{2})?\s*(am|pm)\b", re.IGNORECASE),
    re.compile(r"\bimagine que\b", re.IGNORECASE),
    re.compile(r"\bimagine (that|you)\b", re.IGNORECASE),
    re.compile(r"\bpela (segunda|terceira) vez (nesse|neste|esse|este) m[êe]s\b",
               re.IGNORECASE),
]


def regra_c05(peca):
    out = []
    for campo, texto in peca.campos():
        for rx in RX_C05:
            m = rx.search(texto)
            if m:
                out.append(
                    achado(
                        "C05",
                        campo,
                        recorta(texto, m.start(), m.end()),
                        "corte a cena e va direto a oferta ou a condicao",
                    )
                )
                break
    return out


# ---------------------------------------------------------------------------
# C07  Comentario sobre a propria copy
# ---------------------------------------------------------------------------
RX_C07 = [
    re.compile(r"\ba copy\b", re.IGNORECASE),
    re.compile(r"\bess[ae] vers[ãa]o\b", re.IGNORECASE),
    re.compile(r"\bpor que (isso )?funciona\b", re.IGNORECASE),
    re.compile(r"\baqui est[áa]\b", re.IGNORECASE),
    re.compile(r"\bhere'?s (the|a) (copy|version|draft)\b", re.IGNORECASE),
    re.compile(r"\bthis (copy|version) (is|focuses)\b", re.IGNORECASE),
    re.compile(r"\bwhy (this|it) works\b", re.IGNORECASE),
    re.compile(r"\bsegue (abaixo )?a (copy|vers[ãa]o)\b", re.IGNORECASE),
]


def regra_c07(peca):
    out = []
    for campo, texto in peca.campos():
        for rx in RX_C07:
            m = rx.search(texto)
            if m:
                out.append(
                    achado(
                        "C07",
                        campo,
                        recorta(texto, m.start(), m.end()),
                        "entregue so os campos da peca, sem comentario sobre a copy",
                    )
                )
                break
    return out


# ---------------------------------------------------------------------------
# C10  Antitese
# ---------------------------------------------------------------------------
RX_C10 = [
    re.compile(r"n[ãa]o\s+(e|é)\s+(s[oó]|apenas)\b", re.IGNORECASE),
    re.compile(r"n[ãa]o\s+(s[oó]|apenas)\s+\w+.{0,40}?,\s*(e|é|mas)\b",
               re.IGNORECASE),
    re.compile(r"\bmais (do )?que (um|uma)\b", re.IGNORECASE),
    re.compile(r"(?:n'?t|\bnot)\s+(just|only)\b", re.IGNORECASE),
    re.compile(r"\bit'?s not\b", re.IGNORECASE),
    re.compile(r"\bmore than (a|an|just)\b", re.IGNORECASE),
]


def regra_c10(peca):
    out = []
    for campo, texto in peca.campos():
        for rx in RX_C10:
            m = rx.search(texto)
            if m:
                out.append(
                    achado(
                        "C10",
                        campo,
                        recorta(texto, m.start(), m.end()),
                        "afirme direto o atributo, sem negar antes",
                    )
                )
                break
    return out


# ---------------------------------------------------------------------------
# C11  Triade ornamental
# ---------------------------------------------------------------------------
RX_CLAUSULA = re.compile(r"[.!?;:—–\n]+")
CONECTOR = {"pt-br": ("e",), "en": ("and",)}


def _palavras(s: str) -> list[str]:
    return re.findall(r"[\wÀ-ſ'’]+", s)


def regra_c11(peca):
    out = []
    conectores = CONECTOR[peca.idioma] + CONECTOR["en" if peca.idioma == "pt-br" else "pt-br"]
    for campo, texto in peca.campos_de_prosa():
        for clausula in RX_CLAUSULA.split(texto):
            itens = _triade(clausula, conectores)
            if itens is None:
                continue
            total = sum(len(_palavras(i)) for i in itens)
            if total <= 8:
                out.append(
                    achado(
                        "C11",
                        campo,
                        clausula.strip(),
                        "troque a triade por 1 atributo com prova",
                    )
                )
    return out


def _triade(clausula: str, conectores):
    """Devolve os itens quando a clausula for [item, item, (e|and) item]."""
    partes = [p.strip() for p in clausula.split(",")]
    partes = [p for p in partes if p]
    if len(partes) < 2:
        return None
    idx = None
    for i, p in enumerate(partes):
        primeira = dobra(p).split()
        if primeira and primeira[0] in conectores and i >= 2:
            idx = i
            break
    if idx is not None:
        itens = partes[: idx + 1]
        # o conector nao conta como palavra do item
        itens = itens[:-1] + [" ".join(itens[-1].split()[1:])]
        return itens if len(itens) == 3 else None
    # sem virgula de Oxford: "a, b e c"
    ultimo = partes[-1]
    for con in conectores:
        rx = re.compile(r"\s+" + re.escape(con) + r"\s+", re.IGNORECASE)
        m = rx.search(ultimo)
        if m:
            itens = partes[:-1] + [ultimo[: m.start()].strip(), ultimo[m.end():].strip()]
            return itens if len(itens) == 3 else None
    return None


# ---------------------------------------------------------------------------
# C13, C14, C15  Retorica
# ---------------------------------------------------------------------------
RX_C13 = [
    re.compile(r"\be o melhor\s*:", re.IGNORECASE),
    re.compile(r"\bs[oó] que tem um detalhe\b", re.IGNORECASE),
    re.compile(r"\bmas tem um por[eé]m\b", re.IGNORECASE),
    re.compile(r"\bhere'?s the (best|kicker|catch)\b", re.IGNORECASE),
    re.compile(r"\bbut wait\b", re.IGNORECASE),
    re.compile(r"\bo melhor de tudo\s*:", re.IGNORECASE),
]
RX_C14 = [
    re.compile(r"\bseja (voc[eê] )?\w+ ou\b", re.IGNORECASE),
    re.compile(r"\bpara quem \w+ e para quem\b", re.IGNORECASE),
    re.compile(r"\bwhether you'?re\b", re.IGNORECASE),
    re.compile(r"\bwhether it'?s\b", re.IGNORECASE),
]


def _regra_por_regex(peca, regra, regexes, sugestao, apenas_prosa=True):
    out = []
    campos = peca.campos_de_prosa() if apenas_prosa else peca.campos()
    for campo, texto in campos:
        for rx in regexes:
            m = rx.search(texto)
            if m:
                out.append(achado(regra, campo, recorta(texto, m.start(), m.end()), sugestao))
                break
    return out


def regra_c13(peca):
    return _regra_por_regex(peca, "C13", RX_C13, "afirme direto, sem revelacao teatral")


def regra_c14(peca):
    return _regra_por_regex(peca, "C14", RX_C14, "escolha um uso e um publico")


def regra_c15(peca):
    if not peca.blocos:
        return []
    primeiro = peca.blocos[0].strip()
    if primeiro.endswith("?"):
        return [
            achado(
                "C15",
                "blocos[0]",
                primeiro,
                "troque a pergunta retorica pela situacao concreta do cliente",
            )
        ]
    return []


# ---------------------------------------------------------------------------
# C12, C16, C17, C20 a C26  Lexico
# ---------------------------------------------------------------------------
def regra_lexico(peca, entradas):
    unitarios = []
    densidade = {}
    for campo, texto in peca.campos():
        folded = dobra(texto)
        for e in entradas:
            alvo = texto if e.padrao.startswith("re:") else folded
            for m in e.rx.finditer(alvo):
                if e.modo == "densidade":
                    densidade.setdefault(e.regra, []).append(
                        (campo, recorta(texto, m.start(), m.end()), e.sugestao)
                    )
                else:
                    unitarios.append(
                        achado(e.regra, campo, recorta(texto, m.start(), m.end()), e.sugestao)
                    )
                break  # 1 achado por entrada por campo
    out = list(unitarios)
    for regra, ocorrencias in densidade.items():
        if len(ocorrencias) >= 3:
            campo, trecho, sugestao = ocorrencias[0]
            out.append(
                achado(
                    regra,
                    campo,
                    trecho,
                    f"{len(ocorrencias)} ocorrencias no e-mail: {sugestao}",
                )
            )
    return out


# ---------------------------------------------------------------------------
# C18  Frases de tamanho uniforme
# ---------------------------------------------------------------------------
RX_FRASE = re.compile(r"[.!?]+")


def regra_c18(peca):
    # So vale para o corpo. Assunto, preheader, CTA e alt sao rotulos curtos
    # por natureza (secao 8): media baixa nao e ritmo de maquina.
    frases = []
    for bloco in peca.blocos:
        for f in RX_FRASE.split(bloco):
            n = len(_palavras(f))
            if n >= 3:
                frases.append(n)
    if len(frases) < 4:
        return []
    media = sum(frases) / len(frases)
    if media < 8:
        return []  # e-mail de rotulos, nao de prosa
    desvio = math.sqrt(sum((n - media) ** 2 for n in frases) / len(frases))
    if desvio < 3:
        return [
            achado(
                "C18",
                "blocos",
                f"{len(frases)} frases, media {media:.1f} palavras, desvio {desvio:.1f}",
                "alterne frases de 3 a 5 palavras com frases de 12 a 15",
            )
        ]
    return []


# ---------------------------------------------------------------------------
# C30 a C35  Forma e pontuacao
# ---------------------------------------------------------------------------
RX_EMOJI = re.compile(
    "[\U0001F000-\U0001FAFF←-⇿⌀-⏿☀-➿⬀-⯿️]"
)
RX_INVISIVEL = re.compile("[​‌‍﻿ ⁠]")
RX_FAKE_BOLD = re.compile("[\U0001D400-\U0001D7FF]")
RX_STRONG = re.compile(r"<strong\b", re.IGNORECASE)
RX_PALAVRA_CAP = re.compile(r"\b[A-ZÀ-Ý][a-zà-ÿ]+\b")
RX_RUN_CAIXA_ALTA = re.compile(r"\b[A-ZÀ-Ý]{2,}(?:[\s,]+[A-ZÀ-Ý0-9%]{2,}){5,}")


def regra_c30(peca):
    total = sum(texto.count("!") for _c, texto in peca.campos())
    if total > 1:
        return [
            achado(
                "C30",
                "peca",
                f"{total} exclamacoes",
                "no maximo 1 exclamacao por e-mail, 0 no assunto de marca premium",
            )
        ]
    return []


def regra_c31(peca):
    out = []
    n_assunto = len(RX_EMOJI.findall(peca.assunto))
    limite_assunto = 1 if peca.marca_usa_emoji else 0
    if n_assunto > limite_assunto:
        out.append(
            achado(
                "C31",
                "assunto",
                peca.assunto,
                "emoji no assunto so quando a ficha da marca autoriza, no maximo 1",
            )
        )
    if not peca.marca_usa_emoji:
        for i, b in enumerate(peca.blocos):
            if RX_EMOJI.search(b):
                out.append(
                    achado("C31", f"blocos[{i}]", b, "sem emoji decorativo no corpo")
                )
    return out


def regra_c32(peca):
    out = []
    for i, b in enumerate(peca.blocos):
        n = len(RX_STRONG.findall(b))
        if n > 2:
            out.append(
                achado(
                    "C32",
                    f"blocos[{i}]",
                    f"{n} tags strong no mesmo bloco",
                    "negrito so no codigo do cupom e no valor da oferta",
                )
            )
    return out


def regra_c33(peca):
    out = []
    for campo, texto in peca.campos():
        if RX_INVISIVEL.search(texto):
            out.append(
                achado("C33", campo, texto, "remova caracteres invisiveis de preenchimento")
            )
        elif len(RX_FAKE_BOLD.findall(texto)) >= 4:
            out.append(
                achado("C33", campo, texto, "remova letras Unicode de falso negrito")
            )
    return out


def regra_c34(peca):
    if peca.idioma != "pt-br":
        return []
    out = []
    for campo, texto in peca.campos_de_prosa():
        for trecho in re.split(r"[.!?\n]", texto):
            palavras = trecho.split()
            corrida = 0
            melhor = 0
            for p in palavras:
                limpa = p.strip(".,;:!?()“”\"'")
                if RX_PALAVRA_CAP.fullmatch(limpa):
                    corrida += 1
                    melhor = max(melhor, corrida)
                else:
                    corrida = 0
            if melhor >= 4:
                out.append(
                    achado(
                        "C34",
                        campo,
                        trecho.strip(),
                        "em pt-BR use caixa de frase ou caixa alta total, nunca Title Case",
                    )
                )
                break
    return out


def regra_c35(peca):
    out = []
    for i, b in enumerate(peca.blocos):
        m = RX_RUN_CAIXA_ALTA.search(b)
        if m:
            out.append(
                achado(
                    "C35",
                    f"blocos[{i}]",
                    recorta(b, m.start(), m.end()),
                    "caixa alta so em headline curta, rotulo e botao",
                )
            )
    return out


# ---------------------------------------------------------------------------
# C40 a C47  Especificos de e-mail
# ---------------------------------------------------------------------------
RX_CODIGO_CUPOM = re.compile(r"\b[A-Z][A-Z0-9]{3,19}\b")
RX_VALOR = re.compile(r"(\d\s*%|%\s*\d|R\$\s*\d|US\$\s*\d|\$\s*\d|€\s*\d)")
RX_MERGE = re.compile(r"\{\{\s*([^}]+?)\s*\}\}")
PRAZO = [
    "hoje", "amanha", "ate ", "ate o", "domingo", "segunda", "terca", "quarta",
    "quinta", "sexta", "sabado", "por tempo limitado", "48h", "24h", "72h",
    "ultimo dia", "esta semana", "neste fim de semana", "valido",
    "today", "tomorrow", "through ", "until ", "ends ", "limited time",
    "this week", "last day", "valid",
]
MINIMO = ["acima de", "a partir de", "minimo", "compras acima", "orders over",
          "spend ", "minimum", "aplicado no carrinho", "applied at checkout"]
TETO_BODY = {"welcome": 80, "campanha": 80, "promo": 80, "carrinho": 60,
             "abandono": 60, "editorial": None, "carta": None}


def regra_c40(peca):
    n = len(peca.assunto)
    if n > 60:
        return [
            achado(
                "C40_GRAVE",
                "assunto",
                peca.assunto,
                f"assunto com {n} caracteres: corte para o alvo de 40, com a "
                f"oferta no comeco",
            )
        ]
    if n > 40:
        return [
            achado(
                "C40",
                "assunto",
                peca.assunto,
                f"assunto com {n} caracteres: alvo 40, ideal 25. O limite exato "
                f"esta sob teste A/B (ver docs/pesquisa/a-verificar.md)",
            )
        ]
    return []


def _tokens(texto: str) -> set:
    return {t for t in dobra(texto).split() if len(t) > 2}


def regra_c41(peca):
    if not peca.preheader.strip():
        return [
            achado(
                "C41",
                "preheader",
                "",
                "preheader vazio: complete com condicao, prazo ou produto",
            )
        ]
    a, b = _tokens(peca.assunto), _tokens(peca.preheader)
    if not a or not b:
        return []
    jaccard = len(a & b) / len(a | b)
    if jaccard > 0.6:
        return [
            achado(
                "C41",
                "preheader",
                peca.preheader,
                f"preheader repete o assunto (Jaccard {jaccard:.2f}): complete a "
                f"informacao em vez de repetir",
            )
        ]
    return []


def _tem_oferta(texto: str) -> bool:
    if RX_VALOR.search(texto):
        return True
    for token in RX_CODIGO_CUPOM.findall(texto):
        if any(ch.isdigit() for ch in token):
            return True
    return False


def regra_c42(peca):
    todos = " ".join(t for _c, t in peca.campos())
    texto_vivo = " ".join([peca.assunto, peca.preheader] + peca.blocos)
    if _tem_oferta(todos) and not _tem_oferta(texto_vivo):
        return [
            achado(
                "C42",
                "blocos",
                "",
                "a oferta so aparece na imagem ou no alt: coloque 1 linha de texto "
                "vivo com o valor e o codigo",
            )
        ]
    return []


def regra_c43(peca):
    verbos = set(VERBOS_CTA[peca.idioma])
    out = []
    for i, cta in enumerate(peca.ctas):
        if not cta.strip():
            continue
        primeira = dobra(cta.strip()).split()[0].strip(".,!:;")
        if primeira not in verbos:
            out.append(
                achado(
                    "C43",
                    f"ctas[{i}]",
                    cta,
                    "CTA e verbo de compra mais objeto: 'Comprar com 10% OFF', "
                    "'Ver a colecao'",
                )
            )
    return out


def regra_c44(peca):
    destinos = {u.strip() for u in peca.cta_urls if u and u.strip()}
    if len(destinos) > 1:
        return [
            achado(
                "C44",
                "ctas",
                ", ".join(sorted(destinos)),
                "1 acao principal por e-mail. CTA repetido com o mesmo destino e "
                "permitido",
            )
        ]
    return []


def regra_c45(peca):
    teto = TETO_BODY.get(peca.tipo, 80)
    if teto is None:
        return []
    n = sum(len(_palavras(b)) for b in peca.blocos)
    if n > teto:
        return [
            achado(
                "C45",
                "blocos",
                f"{n} palavras",
                f"orcamento de {teto} palavras para o tipo '{peca.tipo}': corte o "
                f"corpo (editorial e carta sao excecao declarada)",
            )
        ]
    return []


def regra_c46(peca):
    todos = " ".join(t for _c, t in peca.campos())
    if not _tem_oferta(todos):
        return []
    folded = dobra(todos)
    tem_prazo = any(p in folded for p in PRAZO)
    tem_minimo = any(p in folded for p in MINIMO)
    if tem_prazo or tem_minimo:
        return []
    return [
        achado(
            "C46",
            "blocos",
            "",
            "a oferta esta sem condicao: informe prazo, ou minimo, ou "
            "'aplicado no carrinho'",
        )
    ]


def regra_c47(peca):
    out = []
    for campo, texto in peca.campos():
        for m in RX_MERGE.finditer(texto):
            conteudo = m.group(1)
            if "default" not in conteudo.lower() and "|" not in conteudo:
                out.append(
                    achado(
                        "C47",
                        campo,
                        m.group(0),
                        "merge tag sem fallback: use default e garanta que a frase "
                        "funciona sem o nome",
                    )
                )
    return out


# ---------------------------------------------------------------------------
# Execucao
# ---------------------------------------------------------------------------
REGRAS = [
    regra_c01, regra_c02, regra_c03, regra_c04, regra_c05, regra_c07,
    regra_c10, regra_c11, regra_c13, regra_c14, regra_c15, regra_c18,
    regra_c30, regra_c31, regra_c32, regra_c33, regra_c34, regra_c35,
    regra_c40, regra_c41, regra_c42, regra_c43, regra_c44, regra_c45,
    regra_c46, regra_c47,
]
ORDEM_SEV = {"B": 0, "A": 1, "M": 2}


def lint(dados: dict, lexico_dir: str = LEXICO_DIR_PADRAO) -> dict:
    peca = Peca(dados)
    entradas = carrega_lexico(arquivo_lexico(peca.idioma, lexico_dir))
    violacoes = []
    for regra in REGRAS:
        violacoes.extend(regra(peca))
    violacoes.extend(regra_lexico(peca, entradas))
    violacoes.sort(key=lambda v: (ORDEM_SEV[v["severidade"]], v["regra"], v["campo"]))
    bloqueia = any(v["severidade"] == "B" for v in violacoes)
    return {
        "ok": not violacoes,
        "bloqueia": bloqueia,
        "total": len(violacoes),
        "violacoes": violacoes,
    }


def main_codigo(dados: dict, lexico_dir: str = LEXICO_DIR_PADRAO) -> int:
    """Codigo de saida que o CLI usaria para esta peca: 1 se houver B."""
    return 1 if lint(dados, lexico_dir)["bloqueia"] else 0


def formata_texto(resultado: dict) -> str:
    if resultado["ok"]:
        return "lint_copy: sem violacoes."
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
    ap = argparse.ArgumentParser(description="Linter de copy de e-mail (Convertfy)")
    ap.add_argument("arquivo", nargs="?", help="JSON de entrada (default: stdin)")
    ap.add_argument("--json", action="store_true", help="saida em JSON")
    ap.add_argument("--lexico", default=LEXICO_DIR_PADRAO, help="pasta dos lexicos")
    args = ap.parse_args(argv)

    bruto = (
        open(args.arquivo, "r", encoding="utf-8").read()
        if args.arquivo and args.arquivo != "-"
        else sys.stdin.read()
    )
    dados = json.loads(bruto)
    resultado = lint(dados, args.lexico)
    if args.json:
        print(json.dumps(resultado, ensure_ascii=False, indent=2))
    else:
        print(formata_texto(resultado))
    return 1 if resultado["bloqueia"] else 0


if __name__ == "__main__":
    sys.exit(main())
