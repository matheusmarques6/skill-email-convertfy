#!/usr/bin/env python3
"""Testes do lint_email.py.

Rodar:
    python3 -m unittest discover scripts/tests
    python3 scripts/tests/test_lint_email.py

Os casos positivos seguem a secao 8 (calibracao): coluna unica de 600px,
centralizado, caixa alta em rotulo e numero grande de oferta NAO sao vicio.
Os casos negativos seguem a secao 6 (D01 a D20) e a secao 9.2.
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import lint_email  # noqa: E402

BOM = """<!doctype html>
<html lang="pt-BR"><body style="margin:0;background-color:#FFFFFF;">
<div style="display:none;font-size:0;max-height:0;overflow:hidden;">
  17% OFF com o codigo LUXURY17, valido ate domingo.
</div>
<table role="presentation" width="600" cellpadding="0" cellspacing="0"
       border="0" align="center" bgcolor="#FFFFFF">
  <tr><td align="center" style="background-color:#FFFFFF;color:#1A1A1A;
      font-family:Helvetica,Arial,sans-serif;font-size:16px;">
    <a href="https://loja.com.br/club"><img src="hero.jpg" width="600"
         height="400" alt="Relogio de aco com 17% OFF ate domingo"></a>
  </td></tr>
  <tr><td align="center" style="background-color:#FFFFFF;color:#000000;
      font-family:Helvetica,Arial,sans-serif;font-size:16px;">
    17% OFF no primeiro pedido. Codigo LUXURY17, valido ate domingo.
  </td></tr>
  <tr><td align="center" bgcolor="#000000">
    <a href="https://loja.com.br/club"
       style="color:#FFFFFF;font-family:Helvetica,Arial,sans-serif;
              font-size:16px;display:inline-block;padding:14px 28px;">
      COMPRAR AGORA
    </a>
  </td></tr>
  <tr><td align="center" style="background-color:#FFFFFF;color:#1A1A1A;
      font-family:Helvetica,Arial,sans-serif;font-size:12px;">
    Rua Exemplo 100, Sao Paulo.
    <a href="{{unsubscribe_url}}" style="color:#1A1A1A;">Descadastrar</a>
  </td></tr>
</table>
</body></html>"""

RUIM = """<!doctype html>
<html><head><style>
@font-face {font-family:'Geist';src:url(g.woff2);}
.hero {position:absolute;top:0;transform:rotate(2deg);}
</style></head>
<body style="background:#F5F0E1;">
<table role="presentation" width="640" align="center" bgcolor="#F5F0E1">
  <tr><td style="background-color:#F5F0E1;color:#AAAAAA;font-size:16px;">
    Sua oferta chegou. Confira a colecao completa da estacao.
  </td></tr>
  <tr><td style="background-color:#F5F0E1;color:#1A1A1A;">
    [FALTA: preco] e [FALTA: preco] para os dois modelos.
  </td></tr>
  <tr><td><img src="hero.png" width="600" style="border-radius:12px;"></td></tr>
  <tr><td align="center" bgcolor="#4F46E5">
    <a href="https://loja.com/a"><img src="botao.png" width="280" alt=""></a>
  </td></tr>
</table>
<svg width="10" height="10"><circle cx="5" cy="5" r="4"/></svg>
</body></html>"""


def regras(resultado):
    return {v["regra"] for v in resultado["violacoes"]}


class CasoBom(unittest.TestCase):
    def test_peca_limpa_nao_bloqueia(self):
        r = lint_email.lint(BOM)
        self.assertFalse(r["bloqueia"], msg=lint_email.formata_texto(r))

    def test_peca_limpa_sem_violacao(self):
        r = lint_email.lint(BOM)
        self.assertEqual(r["violacoes"], [], msg=lint_email.formata_texto(r))

    def test_container_600_aceito(self):
        self.assertNotIn("E_CONTAINER", regras(lint_email.lint(BOM)))

    def test_caixa_alta_no_botao_nao_e_vicio(self):
        # "COMPRAR AGORA" dentro do botao: secao 8.
        self.assertEqual(lint_email.lint(BOM)["total"], 0)

    def test_fundo_branco_nao_e_bege(self):
        self.assertNotIn("D03", regras(lint_email.lint(BOM)))


class CasoRuim(unittest.TestCase):
    def setUp(self):
        self.r = lint_email.lint(RUIM)
        self.ids = regras(self.r)

    def test_bloqueia(self):
        self.assertTrue(self.r["bloqueia"])

    def test_d18_position_transform_svg_border_radius(self):
        trechos = " ".join(
            v["trecho"] for v in self.r["violacoes"] if v["regra"] == "D18"
        )
        self.assertIn("D18", self.ids)
        self.assertIn("position: absolute", trechos)
        self.assertIn("transform:", trechos)
        self.assertIn("<svg", trechos)
        self.assertIn("border-radius", trechos)

    def test_d17_imagem_sem_alt(self):
        self.assertIn("D17", self.ids)

    def test_contraste_baixo(self):
        self.assertTrue({"D04", "D05"} & self.ids)

    def test_container_errado(self):
        self.assertIn("E_CONTAINER", self.ids)

    def test_preheader_ausente(self):
        self.assertIn("E_PREHEADER", self.ids)

    def test_cta_so_em_imagem(self):
        self.assertIn("E_CTA_IMAGEM", self.ids)

    def test_placeholder_repetido(self):
        self.assertIn("E_PLACEHOLDER", self.ids)

    def test_botao_violeta_e_fundo_bege(self):
        self.assertIn("D01", self.ids)
        self.assertIn("D03", self.ids)


class CoresDaMarca(unittest.TestCase):
    def test_violeta_autorizado_pela_ficha(self):
        r = lint_email.lint(RUIM, cores_marca=["#4F46E5", "#F5F0E1"])
        self.assertNotIn("D01", regras(r))
        self.assertNotIn("D03", regras(r))


class OutrasRegras(unittest.TestCase):
    def test_tamanho_acima_do_clipping_bloqueia(self):
        inchado = BOM.replace(
            "</table>", "<!--" + ("x" * (103 * 1024)) + "--></table>"
        )
        r = lint_email.lint(inchado)
        self.assertIn("E_TAMANHO", regras(r))
        self.assertTrue(r["bloqueia"])

    def test_gradiente_bloqueia(self):
        html = BOM.replace(
            'bgcolor="#000000"',
            'style="background:linear-gradient(90deg,#6D28D9,#2563EB)"',
        )
        r = lint_email.lint(html)
        self.assertIn("D02", regras(r))
        self.assertTrue(r["bloqueia"])

    def test_lorem_ipsum(self):
        html = BOM.replace("Rua Exemplo 100, Sao Paulo.", "Lorem ipsum dolor sit.")
        self.assertIn("E_PLACEHOLDER", regras(lint_email.lint(html)))


class Contrato(unittest.TestCase):
    def test_saida_tem_os_cinco_campos(self):
        for v in lint_email.lint(RUIM)["violacoes"]:
            self.assertEqual(
                sorted(v.keys()),
                ["campo", "regra", "severidade", "sugestao", "trecho"],
            )

    def test_severidades_validas(self):
        for v in lint_email.lint(RUIM)["violacoes"]:
            self.assertIn(v["severidade"], ("B", "A", "M"))



class ContainerLegado(unittest.TestCase):
    """600 e o padrao; 598 e legado aceito com aviso M, nao com erro."""

    BASE = ('<html><body><table role="presentation" width="{w}"><tr>'
            '<td style="color:#000;background:#fff">Oferta 20% OFF codigo X'
            '<span style="display:none">pre</span></td></tr></table></body></html>')

    def _regras(self, largura):
        r = lint_email.lint(self.BASE.format(w=largura))
        return {v["regra"]: v["severidade"] for v in r["violacoes"]}

    def test_600_nao_gera_achado_de_container(self):
        r = self._regras(600)
        self.assertNotIn("E_CONTAINER", r)
        self.assertNotIn("E_CONTAINER_LEGADO", r)

    def test_598_avisa_em_m_e_nao_bloqueia(self):
        r = self._regras(598)
        self.assertEqual(r.get("E_CONTAINER_LEGADO"), "M")
        self.assertNotIn("E_CONTAINER", r)

    def test_largura_fora_do_padrao_e_a(self):
        r = self._regras(640)
        self.assertEqual(r.get("E_CONTAINER"), "A")
        self.assertNotIn("E_CONTAINER_LEGADO", r)


def _peca(miolo: str, head: str = "") -> str:
    return (
        f'<html><head>{head}</head><body>'
        '<span style="display:none">Oferta 10% OFF</span>'
        '<table role="presentation" width="600"><tr><td style="color:#000;'
        f'background:#fff;font-family:Arial,sans-serif;font-size:16px">{miolo}'
        '</td></tr><tr><td style="font-size:12px;color:#333;background:#fff">'
        'Rua Exemplo 100, Sao Paulo, SP, Brasil, CEP 01000-000. '
        '<a href="{{unsubscribe_url}}" style="color:#333">Descadastrar</a>'
        '</td></tr></table></body></html>'
    )


def _sev(html: str) -> dict:
    r = lint_email.lint(html)
    return {v["regra"]: v["severidade"] for v in r["violacoes"]}


class CamadaVisual(unittest.TestCase):
    """D21, D26 a D29: catalogadas como `revisar` (D-003), avisam em M."""

    def test_d21_imagem_grande_sem_link(self):
        r = _sev(_peca('<img src="h.jpg" width="600" alt="Bota com 10% OFF">'))
        self.assertEqual(r.get("D21"), "M")

    def test_d21_imagem_linkada_passa(self):
        r = _sev(_peca('<a href="https://l.com"><img src="h.jpg" width="600" '
                       'alt="Bota com 10% OFF"></a>'))
        self.assertNotIn("D21", r)

    def test_d21_logo_pequeno_sem_link_passa(self):
        r = _sev(_peca('<img src="logo.png" width="140" alt="Loja">'))
        self.assertNotIn("D21", r)

    def test_d26_corpo_pequeno(self):
        r = _sev(_peca('<p style="font-size:12px">Frete gratis para todo o '
                       'Brasil em pedidos acima de cem reais nesta semana.</p>'))
        self.assertEqual(r.get("D26"), "M")

    def test_d26_rotulo_curto_de_12px_passa(self):
        # Selo e legenda de preco: rotulo curto, nao e corpo.
        r = _sev(_peca('<span style="font-size:12px">ATE DOMINGO</span>'))
        self.assertNotIn("D26", r)

    def test_d26_rodape_de_12px_passa(self):
        # O _peca ja traz rodape de 12px antes do descadastro, no mesmo td.
        self.assertNotIn("D26", _sev(_peca("Oferta de 10% OFF hoje.")))

    def test_d26_rodape_abaixo_de_11px(self):
        html = _peca("Oferta de 10% OFF hoje.").replace("font-size:12px",
                                                         "font-size:9px")
        self.assertEqual(_sev(html).get("D26"), "M")

    def test_d26_pt_convertido(self):
        # 9pt = 12px, e frase longa: corpo pequeno.
        r = _sev(_peca('<p style="font-size:9pt">Frete gratis para todo o '
                       'Brasil em pedidos acima de cem reais nesta semana.</p>'))
        self.assertIn("D26", r)

    def test_d27_text_shadow(self):
        r = _sev(_peca('<h1 style="text-shadow:0 2px 4px #000">10% OFF</h1>'))
        self.assertEqual(r.get("D27"), "M")

    def test_d28_tres_familias(self):
        r = _sev(_peca(
            '<p style="font-family:Montserrat,Arial,sans-serif">A</p>'
            '<p style="font-family:Georgia,serif">B</p>'
            '<p style="font-family:\'Courier New\',monospace">C</p>'))
        self.assertEqual(r.get("D28"), "M")

    def test_d28_duas_familias_passa(self):
        # O _peca ja declara Arial no td. Montserrat com fallback Arial mais
        # Arial sozinha: duas familias.
        r = _sev(_peca(
            '<p style="font-family:Montserrat,Arial,sans-serif">A</p>'
            '<p style="font-family:Arial,sans-serif">B</p>'))
        self.assertNotIn("D28", r)

    def test_d29_duas_cores_de_botao(self):
        r = _sev(_peca(
            '<a href="https://l.com/a" style="background:#111111;color:#fff;'
            'padding:16px 32px;display:inline-block">COMPRAR</a>'
            '<a href="https://l.com/b" style="background:#C8102E;color:#fff;'
            'padding:16px 32px;display:inline-block">VER TUDO</a>'))
        self.assertEqual(r.get("D29"), "M")

    def test_d29_botao_fantasma_nao_conta(self):
        r = _sev(_peca(
            '<a href="https://l.com/a" style="background:#111111;color:#fff;'
            'padding:16px 32px;display:inline-block">COMPRAR</a>'
            '<a href="https://l.com/b" style="background:#FFFFFF;color:#111;'
            'border:2px solid #111;padding:14px 30px;display:inline-block">'
            'VER TUDO</a>'))
        self.assertNotIn("D29", r)

    def test_camada_visual_nunca_bloqueia(self):
        html = _peca(
            '<img src="h.jpg" width="600" alt="Bota com 10% OFF">'
            '<h1 style="text-shadow:0 1px 0 #000">X</h1>')
        self.assertFalse(lint_email.lint(html)["bloqueia"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
