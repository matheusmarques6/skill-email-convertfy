"""A versao do catalogo e derivada do conteudo, nao escrita a mao."""

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent


def _mod(nome, arq):
    s = importlib.util.spec_from_file_location(nome, RAIZ / "scripts" / arq)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


vc = _mod("versao_catalogo", "versao_catalogo.py")


class VersaoCatalogo(unittest.TestCase):
    def test_formato(self):
        v = vc.versao()
        self.assertTrue(v.startswith("cat-"), v)
        self.assertEqual(len(v), 12, v)

    def test_estavel_entre_chamadas(self):
        self.assertEqual(vc.versao(), vc.versao())

    def test_todas_as_fontes_existem(self):
        d = vc.calcula()
        self.assertEqual(d["fontes_ausentes"], [],
                         "fonte de regra sumiu: a versao ficaria cega para ela")

    def test_cobre_as_familias_de_regra(self):
        f = vc.calcula()["familias"]
        for p in ("C", "D", "P", "R"):
            self.assertGreater(f[p], 0, f"familia {p} sem regra detectada")

    def test_muda_quando_a_regra_muda(self):
        """O ponto do carimbo: mexeu no lexico, a versao anda."""
        lex = RAIZ / "shared" / "lexico" / "pt-br.txt"
        antes = vc.versao()
        original = lex.read_bytes()
        try:
            lex.write_bytes(original + b"\nC20 | teste-de-versao | corte | unitario\n")
            self.assertNotEqual(vc.versao(), antes)
        finally:
            lex.write_bytes(original)
        self.assertEqual(vc.versao(), antes, "nao voltou ao estado original")


class CarimboNoLint(unittest.TestCase):
    def test_lint_copy_carimba(self):
        peca = {"idioma": "pt-br", "assunto": "Oferta", "preheader": "Codigo X.",
                "blocos": ["Ver a oferta."], "ctas": ["Comprar"], "alts": [],
                "brief_numbers": []}
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False,
                                         encoding="utf-8") as f:
            json.dump(peca, f)
            caminho = f.name
        r = subprocess.run([sys.executable, str(RAIZ / "scripts" / "lint_copy.py"),
                            "--json", caminho], capture_output=True, text=True)
        d = json.loads(r.stdout)
        self.assertEqual(d["versao_catalogo"], vc.versao())

    def test_lint_email_carimba(self):
        html = ('<html><body><table role="presentation" width="600"><tr>'
                '<td style="color:#000;background:#fff">'
                '<span style="display:none">pre</span>20% OFF codigo X'
                '</td></tr></table></body></html>')
        with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False,
                                         encoding="utf-8") as f:
            f.write(html)
            caminho = f.name
        r = subprocess.run([sys.executable, str(RAIZ / "scripts" / "lint_email.py"),
                            "--json", caminho], capture_output=True, text=True)
        d = json.loads(r.stdout)
        self.assertEqual(d["versao_catalogo"], vc.versao())


if __name__ == "__main__":
    unittest.main()
