"""O revisor e executavel: o contexto limpo e a nota sao verificaveis."""

import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
_s = importlib.util.spec_from_file_location("revisar", RAIZ / "scripts" / "revisar.py")
rev = importlib.util.module_from_spec(_s)
_s.loader.exec_module(rev)

PNG = (b"\x89PNG\r\n\x1a\n" + b"\x00" * 40)


def _peca(tmp, lint_copy=None, lint_email=None, papel="pico"):
    d = Path(tmp) / "loja-x" / "peca"
    d.mkdir(parents=True)
    for n in ("desktop-600.png", "mobile-375.png", "dark-600.png"):
        (d / n).write_bytes(PNG)
    (d / "relatorio.md").write_text(f"| Papel | {papel} |", encoding="utf-8")
    (d / "email.html").write_text("<html></html>", encoding="utf-8")
    (d / "copy.json").write_text("{}", encoding="utf-8")
    (d / "lint_copy.json").write_text(
        json.dumps(lint_copy or {"violacoes": []}), encoding="utf-8")
    (d / "lint_email.json").write_text(
        json.dumps(lint_email or {"violacoes": []}), encoding="utf-8")
    return d


def _responde(d, valor=True, **extra):
    f = d / "revisao" / "revisao.json"
    o = json.loads(f.read_text(encoding="utf-8"))
    o["respostas"] = {k: extra.get(k, valor) for k in o["respostas"]}
    f.write_text(json.dumps(o, ensure_ascii=False), encoding="utf-8")


class ContextoLimpo(unittest.TestCase):
    def test_leva_so_pngs_e_ficha(self):
        with tempfile.TemporaryDirectory() as t:
            d = _peca(t)
            r = rev.preparar(d)
            nomes = {p.name for p in (d / "revisao").iterdir()}
            self.assertEqual(
                nomes - {"revisao.json"},
                {"desktop-600.png", "mobile-375.png", "dark-600.png"})

    def test_nao_vaza_html_brief_nem_copy(self):
        """Quem sabe a intencao le a intencao, nao o resultado."""
        with tempfile.TemporaryDirectory() as t:
            d = _peca(t)
            r = rev.preparar(d)
            self.assertEqual(r["vazou"], [])
            for proibido in ("email.html", "copy.json", "relatorio.md"):
                self.assertFalse((d / "revisao" / proibido).exists(), proibido)


class Nota(unittest.TestCase):
    def test_zero_defeito_com_qualidade_baixa_trava_em_6(self):
        """O ponto do padrao: nao errar nao e o mesmo que acertar."""
        with tempfile.TemporaryDirectory() as t:
            d = _peca(t)
            rev.preparar(d)
            _responde(d, valor=False)
            o = rev.pontua(d)
            self.assertEqual(o["defeitos"], {"B": 0, "A": 0, "M": 0})
            self.assertEqual(o["nota"], 6)
            self.assertFalse(o["aprovada"])

    def test_zero_defeito_com_qualidade_cheia_da_10(self):
        with tempfile.TemporaryDirectory() as t:
            d = _peca(t)
            rev.preparar(d)
            _responde(d, valor=True)
            o = rev.pontua(d)
            self.assertEqual(o["nota"], 10)
            self.assertTrue(o["aprovada"])

    def test_violacao_b_trava_em_3(self):
        with tempfile.TemporaryDirectory() as t:
            d = _peca(t, lint_copy={"violacoes": [
                {"regra": "C01", "severidade": "B"}]})
            rev.preparar(d)
            _responde(d, valor=True)
            o = rev.pontua(d)
            self.assertEqual(o["nota"], 3)
            self.assertFalse(o["aprovada"])

    def test_recusa_revisao_incompleta(self):
        with tempfile.TemporaryDirectory() as t:
            d = _peca(t)
            rev.preparar(d)
            with self.assertRaises(SystemExit):
                rev.pontua(d)

    def test_marca_revisao_velha_quando_o_catalogo_anda(self):
        with tempfile.TemporaryDirectory() as t:
            d = _peca(t)
            rev.preparar(d)
            _responde(d, valor=True)
            f = d / "revisao" / "revisao.json"
            o = json.loads(f.read_text(encoding="utf-8"))
            o["versao_catalogo"] = "cat-00000000"
            f.write_text(json.dumps(o, ensure_ascii=False), encoding="utf-8")
            self.assertTrue(rev.pontua(d)["revisao_velha"])


class Estado(unittest.TestCase):
    def test_sem_veredito_nao_esta_revisada(self):
        with tempfile.TemporaryDirectory() as t:
            self.assertFalse(rev.estado(_peca(t))["revisada"])


if __name__ == "__main__":
    unittest.main()
