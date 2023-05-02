from django.test import TestCase
from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer


class ProgramaSerializerTestCase(TestCase):
    '''Teste para verificar os campos que estão sendo serializados'''
    def setUp(self): # setUp é executado antes de cada teste
        self.programa = Programa(
            titulo='Procurando Ninguém em latim',
            tipo='F',
            data_lancamento='2003-07-04',
            likes=234,
            dislikes=12
        )
        self.serializer = ProgramaSerializer(instance=self.programa) # instance é o objeto que será serializado

    def test_verifica_campos_serializados(self):
        """Teste que verifica os campos que estão sendo serializados"""
        data = self.serializer.data # data é um OrderedDict
        self.assertEqual(set(data.keys()), set(['titulo', 'tipo', 'data_lancamento', 'likes'])) # dislikes não está sendo serializado
    
    def test_verifica_conteudo_dos_campos_serializados(self):
        """Teste que verifica o conteúdo dos campos serializados"""
        data = self.serializer.data # data é um OrderedDict
        self.assertEqual(data['titulo'], self.programa.titulo) # self.programa.titulo é um atributo do modelo Programa
        self.assertEqual(data['data_lancamento'], self.programa.data_lancamento) # self.programa.data_lancamento é um atributo do modelo Programa
        self.assertEqual(data['tipo'], self.programa.tipo) # self.programa.tipo é um atributo do modelo Programa
        self.assertEqual(data['likes'], self.programa.likes) # self.programa.likes é um atributo do modelo Programa