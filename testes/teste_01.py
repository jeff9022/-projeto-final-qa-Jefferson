import unittest

# Função que vamos testar
def multiplicar(a, b):
    return a * b

# Classe de teste unitário
class TesteMultiplicacao(unittest.TestCase):
    
    def test_multiplicacao_positivos(self):
        self.assertEqual(multiplicar(2, 3), 6)

    def test_multiplicacao_zero(self):
        self.assertEqual(multiplicar(0, 5), 0)

    def test_multiplicacao_negativos(self):
        self.assertEqual(multiplicar(-2, 3), -6)

# Executa os testes
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)

