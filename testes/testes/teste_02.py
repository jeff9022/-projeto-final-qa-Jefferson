import unittest

# Função que já existia no sistema
def somar(a, b):
    return a + b

# Teste de regressão
class TesteRegressaoSoma(unittest.TestCase):

    def test_soma_regressao(self):
        # Testa se a função ainda soma corretamente após possíveis mudanças
        self.assertEqual(somar(10, 5), 15)
        self.assertEqual(somar(-3, 3), 0)
        self.assertEqual(somar(0, 0), 0)

# Executa os testes
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
