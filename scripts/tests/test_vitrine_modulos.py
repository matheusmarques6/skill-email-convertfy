#!/usr/bin/env python3
"""Testes da vitrine de modulos (skills/email-design/references/modulos-ecommerce.md).

O trecho de HTML de referencia so fica no arquivo se passa no lint. Este
teste monta todos os modulos com valores de exemplo, sem renderizar, e
exige zero achado, inclusive M: a vitrine e o caso bom.

Rodar:
    python3 -m unittest discover scripts/tests
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import lint_email  # noqa: E402
import vitrine_modulos as vm  # noqa: E402


class Vitrine(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lista = vm.modulos()
        cls.html, cls.faltando = vm.monta(cls.lista)
        cls.r = lint_email.lint(cls.html)

    def test_extrai_os_modulos(self):
        slugs = [s for s, _ in self.lista]
        self.assertGreaterEqual(len(slugs), 14)
        self.assertEqual(len(slugs), len(set(slugs)), "slug repetido")

    def test_todo_slot_tem_valor_de_exemplo(self):
        self.assertEqual(self.faltando, set())

    def test_todo_slot_declarado_tem_sublinhado(self):
        self.assertEqual(vm.slots_problematicos(), [])

    def test_lint_sem_nenhum_achado(self):
        self.assertEqual(self.r["violacoes"], [],
                         msg=lint_email.formata_texto(self.r))

    def test_espaco_so_da_escala(self):
        # espaco-e-ritmo.md: 4 8 12 16 24 32 40 48 64, e nada fora disso.
        import re
        escala = {0, 4, 8, 12, 16, 24, 32, 40, 48, 64}
        fora = set()
        for slug, html in self.lista:
            for _prop, valor in re.findall(
                    r"(padding|margin(?:-top|-bottom)?)\s*:\s*([^;\"]+)", html):
                for n in re.findall(r"(\d+)px", valor):
                    if int(n) not in escala:
                        fora.add(f"{slug}: {n}px")
        self.assertEqual(fora, set())

    def test_slot_sem_sublinhado_e_pego(self):
        texto = "Slots: `SAUDACAO`, `URL_DO_CTA`.\n\n"
        self.assertEqual(vm.slots_problematicos(texto), ["SAUDACAO"])

    def test_cada_modulo_passa_sozinho(self):
        # Um modulo que so passa porque o vizinho tem o preheader ou o
        # descadastro esconde defeito. Cada um, com a casca, sozinho.
        for slug, html in self.lista:
            with self.subTest(modulo=slug):
                peca, falta = vm.monta([(slug, html)])
                r = lint_email.lint(peca)
                self.assertFalse(falta)
                self.assertEqual(r["violacoes"], [],
                                 msg=f"{slug}: " + lint_email.formata_texto(r))


if __name__ == "__main__":
    unittest.main(verbosity=2)
