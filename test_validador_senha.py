import unittest
from validador_senha import ValidadorSenha

class TestValidadorSenha(unittest.TestCase):
    def setUp(self):
        self.validador = ValidadorSenha()

    def test_senha_invalida_curta(self):
        resultado = self.validador.validar("abc")
        self.assertFalse(resultado["valida"])
        self.assertIn("A senha deve ter pelo menos 8 caracteres", resultado["erros"])

if _name_ == "_main_":
    unittest.main()