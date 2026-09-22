#!/usr/bin/env python3
"""Testes do lint_copy.py.

Rodar:
    python3 -m unittest discover scripts/tests
    python3 scripts/tests/test_lint_copy.py

Os casos NEGATIVOS vem da secao 2.3 (contaminacao do corpus humano) e da
secao 1 (o que a Convertfy ja rejeitou) de
docs/pesquisa/pesquisa-vicios-ia-email.md.
Os casos POSITIVOS vem da secao 8 (calibracao) e da secao 2.2 (padroes humanos
que a skill deve copiar). Falso positivo neles e falha de teste.
"""

import copy
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import lint_copy  # noqa: E402

TRAVESSAO = "—"

BASE_EN = {
    "idioma": "en",
    "tipo": "welcome",
    "assunto": "WELCOME10 for your first order",
    "preheader": "Use it today, one order per customer.",
    "blocos": [
        "Use code WELCOME10 today and start your AB BIO® routine with savings.",
        "If your mattress feels almost right (but you still wake up tired), "
        "let's fix that.",
        "Cruelty Free / Women Founded / Ethically Sourced",
    ],
    "ctas": [{"texto": "Shop now", "url": "https://loja.com/new"}],
    "alts": ["WELCOME10: 10% off the first order"],
    "brief_numbers": ["10"],
}

BASE_PT = {
    "idioma": "pt-BR",
    "tipo": "campanha",
    "assunto": "17% OFF na entrada do Luxury Club",
    "preheader": "Codigo LUXURY17, valido ate domingo.",
    "blocos": [
        "Que bom ter voce aqui.",
        "Acessorios, roupas, relogios e sapatos premium com 17% OFF no "
        "primeiro pedido.",
        "Use o codigo LUXURY17 no carrinho. Valido ate domingo.",
    ],
    "ctas": [
        {"texto": "Comprar agora", "url": "https://loja.com.br/club"},
        {"texto": "Comprar agora", "url": "https://loja.com.br/club"},
    ],
    "alts": ["17% OFF na entrada do Luxury Club"],
    "brief_numbers": ["17"],
}

# Regras que denunciam vicio de IA na copy. Nenhuma pode disparar num caso
# positivo. As demais (C40 a C47) sao completude de peca, nao vicio de IA.
REGRAS_DE_VICIO = {
    "C01", "C02", "C03", "C04", "C05", "C06", "C07",
    "C10", "C11", "C12", "C13", "C14", "C15", "C16", "C17", "C18", "C19",
    "C20", "C21", "C22", "C23", "C24", "C25", "C26",
    "C30", "C31", "C32", "C33", "C34", "C35",
}


def roda(payload):
    return lint_copy.lint(payload)


def regras(resultado):
    return {v["regra"] for v in resultado["violacoes"]}


def com_bloco(base, texto):
    p = copy.deepcopy(base)
    p["blocos"] = list(p["blocos"]) + [texto]
    return p


class CasosPositivos(unittest.TestCase):
    """Secao 8 e secao 2.2: o lint nao pode acusar nada aqui."""

    def test_base_en_limpa(self):
        r = roda(BASE_EN)
        self.assertEqual(r["violacoes"], [], msg=lint_copy.formata_texto(r))
        self.assertFalse(r["bloqueia"])

    def test_base_pt_limpa(self):
        r = roda(BASE_PT)
        self.assertEqual(r["violacoes"], [], msg=lint_copy.formata_texto(r))
        self.assertFalse(r["bloqueia"])

    def test_oferta_em_texto_com_codigo(self):
        # "Use code WELCOME10 today and start your AB BIO(R) routine with savings."
        r = roda(BASE_EN)
        self.assertFalse(regras(r) & REGRAS_DE_VICIO)

    def test_reconhecimento_de_problema_helix(self):
        p = copy.deepcopy(BASE_EN)
        p["blocos"] = [
            "If your mattress feels almost right (but you still wake up tired), "
            "let's fix that.",
            "Use code WELCOME10 today, one order per customer.",
        ]
        self.assertFalse(regras(roda(p)) & REGRAS_DE_VICIO)

    def test_rotulos_curtos_com_barra(self):
        p = copy.deepcopy(BASE_EN)
        p["blocos"] = [
            "Cruelty Free / Women Founded / Ethically Sourced",
            "Use code WELCOME10 today, one order per customer.",
        ]
        self.assertFalse(regras(roda(p)) & REGRAS_DE_VICIO)

    def test_caixa_alta_em_headline_curta(self):
        p = copy.deepcopy(BASE_PT)
        p["blocos"] = ["FRETE GRATIS HOJE", "Codigo LUXURY17 no carrinho."]
        self.assertNotIn("C35", regras(roda(p)))
        self.assertNotIn("C34", regras(roda(p)))

    def test_cta_repetido_com_mesmo_destino(self):
        # BASE_PT ja tem 2 CTAs identicos com o mesmo destino.
        self.assertNotIn("C44", regras(roda(BASE_PT)))

    def test_boas_vindas_pronta_seguida_da_oferta(self):
        p = copy.deepcopy(BASE_PT)
        p["tipo"] = "welcome"
        p["blocos"] = [
            "Que bom ter voce aqui.",
            "17% OFF no primeiro pedido com o codigo LUXURY17, valido ate domingo.",
        ]
        self.assertFalse(regras(roda(p)) & REGRAS_DE_VICIO)

    def test_numero_grande_de_oferta_nao_e_numero_inventado(self):
        p = copy.deepcopy(BASE_PT)
        p["blocos"] = ["50% OFF hoje com o codigo LUXURY17."]
        self.assertNotIn("C02", regras(roda(p)))

    def test_paragrafo_unico_de_explicacao(self):
        p = copy.deepcopy(BASE_PT)
        p["blocos"] = [
            "Que bom ter voce aqui.",
            "O relogio tem caixa de aco 316L, pulseira de couro e resistencia "
            "de 5 ATM, o suficiente para lavar as maos e tomar banho sem tirar "
            "do pulso, com 17% OFF ate domingo no codigo LUXURY17.",
        ]
        r = roda(p)
        self.assertNotIn("C45", regras(r))


class CasosNegativosContaminacao(unittest.TestCase):
    """Secao 2.3: linhas do proprio corpus humano que o lint tem que reprovar."""

    def test_nao_apenas_treina_transforma(self):
        p = com_bloco(BASE_EN, "Together, they don't just train you, "
                               "they transform you.")
        r = regras(roda(p))
        self.assertIn("C10", r)
        self.assertIn("C21", r)

    def test_travessao_mais_triade(self):
        p = com_bloco(
            BASE_EN,
            "A science-backed ritual for the bold" + TRAVESSAO
            + "reset, recharge, and perform at your peak.",
        )
        r = roda(p)
        ids = regras(r)
        self.assertIn("C01", ids)
        self.assertIn("C11", ids)
        self.assertIn("C26", ids)
        self.assertTrue(r["bloqueia"])

    def test_triade_ritmica(self):
        p = com_bloco(BASE_EN, "perform better, recover faster, and "
                               "transform deeper")
        ids = regras(roda(p))
        self.assertIn("C11", ids)
        self.assertIn("C21", ids)

    def test_jornada_e_possibilidades_ilimitadas(self):
        p = com_bloco(BASE_EN, "Your journey with DYC is just beginning, and "
                               "the possibilities are limitless.")
        ids = regras(roda(p))
        self.assertIn("C21", ids)
        self.assertIn("C12", ids)

    def test_reacenda_redefina_retorne(self):
        p = com_bloco(BASE_EN, "Reignite your routine, reset your goals, and "
                               "return stronger, no pressure, just results.")
        self.assertIn("C11", regras(roda(p)))


class CasosNegativosConvertfy(unittest.TestCase):
    """Secao 1: o que a Convertfy ja rejeitou em producao."""

    def test_travessao_bloqueia(self):
        p = copy.deepcopy(BASE_PT)
        p["blocos"] = ["Sua oferta chegou " + TRAVESSAO + " aproveite."]
        r = roda(p)
        self.assertIn("C01", regras(r))
        self.assertTrue(r["bloqueia"])
        self.assertEqual(lint_copy.main_codigo(p), 1)

    def test_numero_inventado_bloqueia(self):
        p = copy.deepcopy(BASE_PT)
        p["blocos"] = ["Ja somos 32.541 clientes ativos.", "17% OFF ate domingo."]
        r = roda(p)
        self.assertIn("C02", regras(r))
        self.assertTrue(r["bloqueia"])

    def test_assunto_que_simula_transacao_bloqueia(self):
        p = copy.deepcopy(BASE_PT)
        p["assunto"] = "(RE): confirmacao do seu pedido"
        r = roda(p)
        self.assertIn("C03", regras(r))
        self.assertTrue(r["bloqueia"])

    def test_assunto_que_simula_transacao_em_ingles_bloqueia(self):
        """C03 e B e vale nas duas linguas.

        A grafia "was approved" escapava porque so "has been" estava
        coberta em ingles, enquanto o pt-BR ja cobria "pedido foi".
        """
        for assunto in (
            "Your order was approved",
            "Your order is confirmed",
            "Your order has been shipped",
            "Your order was reviewed",
        ):
            with self.subTest(assunto=assunto):
                p = copy.deepcopy(BASE_EN)
                p["assunto"] = assunto
                r = roda(p)
                self.assertIn("C03", regras(r))
                self.assertTrue(r["bloqueia"])

    def test_cupom_no_idioma_errado_bloqueia(self):
        p = copy.deepcopy(BASE_EN)
        p["blocos"] = ["Use code PEDIDO18 today for 18% off."]
        p["brief_numbers"] = ["18"]
        r = roda(p)
        self.assertIn("C04", regras(r))
        self.assertTrue(r["bloqueia"])

    def test_cena_fabricada_bloqueia(self):
        p = copy.deepcopy(BASE_PT)
        p["blocos"] = ["Sao 11 de novembro. 7:15 da manha."]
        p["brief_numbers"] = ["11", "7", "15"]
        r = roda(p)
        self.assertIn("C05", regras(r))
        self.assertTrue(r["bloqueia"])

    def test_superlativo_vazio(self):
        p = copy.deepcopy(BASE_PT)
        p["blocos"] = ["Descontos extraordinarios ate domingo.",
                       "17% OFF com o codigo LUXURY17."]
        self.assertIn("C20", regras(roda(p)))

    def test_cliche_de_rebranding(self):
        p = copy.deepcopy(BASE_PT)
        p["blocos"] = ["Uma Nova Era Comeca.", "17% OFF ate domingo."]
        ids = regras(roda(p))
        self.assertIn("C26", ids)
        self.assertIn("C34", ids)

    def test_comentario_sobre_a_propria_copy_bloqueia(self):
        p = copy.deepcopy(BASE_PT)
        p["blocos"] = ["A copy e centrada em beneficios.", "17% OFF ate domingo."]
        r = roda(p)
        self.assertIn("C07", regras(r))
        self.assertTrue(r["bloqueia"])

    def test_body_longo_em_campanha(self):
        p = copy.deepcopy(BASE_PT)
        p["blocos"] = [("Palavra " * 100).strip() + " 17% OFF ate domingo."]
        self.assertIn("C45", regras(roda(p)))


class RegrasDeEmail(unittest.TestCase):
    def test_preheader_repete_assunto(self):
        p = copy.deepcopy(BASE_PT)
        p["preheader"] = "17% OFF na entrada do Luxury Club hoje"
        self.assertIn("C41", regras(roda(p)))

    def test_preheader_vazio(self):
        p = copy.deepcopy(BASE_PT)
        p["preheader"] = ""
        self.assertIn("C41", regras(roda(p)))

    def test_oferta_so_na_imagem(self):
        p = copy.deepcopy(BASE_PT)
        p["assunto"] = "Sua entrada no Luxury Club"
        p["preheader"] = "Codigo no carrinho, valido ate domingo."
        p["blocos"] = ["Que bom ter voce aqui."]
        p["alts"] = ["17% OFF ate domingo com o codigo LUXURY17"]
        self.assertIn("C42", regras(roda(p)))

    def test_merge_tag_sem_fallback(self):
        p = copy.deepcopy(BASE_PT)
        p["blocos"] = ["Oi {{first_name}}, 17% OFF ate domingo."]
        self.assertIn("C47", regras(roda(p)))

    def test_dois_ctas_com_destinos_diferentes(self):
        p = copy.deepcopy(BASE_PT)
        p["ctas"] = [
            {"texto": "Comprar agora", "url": "https://loja.com.br/a"},
            {"texto": "Ver colecao", "url": "https://loja.com.br/b"},
        ]
        self.assertIn("C44", regras(roda(p)))

    def test_assunto_longo(self):
        p = copy.deepcopy(BASE_PT)
        p["assunto"] = ("Confira agora a nossa selecao de acessorios premium com "
                        "condicao especial")
        self.assertIn("C40", regras(roda(p)))

    def test_ritmo_metronomico(self):
        p = copy.deepcopy(BASE_PT)
        p["tipo"] = "editorial"
        p["blocos"] = [
            "O relogio chega com caixa de aco e pulseira de couro legitimo. "
            "A resistencia de agua cobre banho e chuva sem nenhum problema. "
            "O mostrador tem indice aplicado e ponteiro luminoso de facil "
            "leitura. A garantia da loja cobre dois anos de uso normal diario."
        ]
        self.assertIn("C18", regras(roda(p)))

    def test_emoji_no_corpo(self):
        p = copy.deepcopy(BASE_PT)
        p["blocos"] = ["17% OFF ate domingo ✅"]
        self.assertIn("C31", regras(roda(p)))

    def test_caractere_invisivel(self):
        p = copy.deepcopy(BASE_PT)
        p["preheader"] = "Ate 40% OFF ate domingo.​​​"
        self.assertIn("C33", regras(roda(p)))


class Contrato(unittest.TestCase):
    def test_saida_tem_os_cinco_campos(self):
        p = copy.deepcopy(BASE_PT)
        p["blocos"] = ["Sua oferta chegou " + TRAVESSAO + " aproveite."]
        for v in roda(p)["violacoes"]:
            self.assertEqual(
                sorted(v.keys()),
                ["campo", "regra", "severidade", "sugestao", "trecho"],
            )

    def test_exit_code_zero_sem_violacao_b(self):
        self.assertEqual(lint_copy.main_codigo(BASE_PT), 0)

    def test_severidades_validas(self):
        p = copy.deepcopy(BASE_PT)
        p["blocos"] = ["Uma Nova Era Comeca " + TRAVESSAO + " 32.541 clientes."]
        for v in roda(p)["violacoes"]:
            self.assertIn(v["severidade"], ("B", "A", "M"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
