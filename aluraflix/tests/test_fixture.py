from django.test import TestCase
from aluraflix.models import Programa


class FixtureDataTestCase(TestCase):
    '''Testes com dados carregados por fixtures'''
    fixtures = ['programas_iniciais.json']

    def test_verifica_carregamento_da_fixture(self):
        '''Teste se a fixture foi carregada corretamente'''
        programa_buscado = Programa.objects.get(pk=1) # busca o programa com id 1
        todos_os_programas = Programa.objects.all() # busca todos os programas
        self.assertEqual(programa_buscado.titulo, 'Coisas bizarras')
        self.assertEqual(len(todos_os_programas), 9)
        