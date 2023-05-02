from django.test import TestCase
from aluraflix.models import Programa

class ProgramaModelTestCase(TestCase):
    '''Teste para verificar os atributos de um programa'''
    def setUp(self):
        '''Método que é executado antes de cada teste'''
        self.programa = Programa(
            titulo='Procurando Ninguém em latim',
            data_lancamento = '2003-07-04'
        ) # Programa é um modelo do Django

    def test_verifica_atributos_do_programa(self):
        """Teste que verifica os atributos de um programa com valores default"""
        self.assertEqual(self.programa.titulo, 'Procurando Ninguém em latim') # self.programa.titulo é um atributo do modelo Programa
        self.assertEqual(self.programa.tipo, 'F') # self.programa.tipo é um atributo do modelo Programa com valor default
        self.assertEqual(self.programa.data_lancamento, '2003-07-04') # self.programa.data_lancamento é um atributo do modelo Programa
        self.assertEqual(self.programa.likes, 0) # self.programa.likes é um atributo do modelo Programa com valor default
        self.assertEqual(self.programa.dislikes, 0) # self.programa.dislikes é um atributo do modelo Programa com valor default
