import unittest

# Função que verifica se uma palavra está presente na frase
def contem_palavra(frase, palavra):
    return palavra in frase

# Classe de teste
class TesteString(unittest.TestCase):
    
    def test_palavra_presente(self):
        self.assertTrue(contem_palavra("Quality Assurance é muito importante", "importante"))

    def test_palavra_ausente(self):
        self.assertFalse(contem_palavra("Aprendendo testes em Python", "Java"))

# Executa os testes
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
