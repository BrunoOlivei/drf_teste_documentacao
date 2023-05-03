from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status


class AuthenticationTestCase(APITestCase):
    
    def setUp(self):
        self.list_url = reverse('programas-list') # cria a url para a listagem de programas
        self.user = User.objects.create_user(username='alura', password='alura123')

    def test_autenticacao_user_com_credenciais_corretas(self):
        """Teste que verifica a autenticacao de um user com as credenciais corretas"""
        user = authenticate(username='alura', password='alura123') # cria um user com as credenciais corretas
        self.assertTrue((user is not None) and user.is_authenticated) # verifica se usuário não é nulo e se está autenticado

    def test_requisicao_get_nao_autorizada(self):
        """Teste que verifica uma requisição GET não autorizada"""
        response = self.client.get(self.list_url) # faz uma requisição GET sem autenticacao
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED) # verifica se o status code é 401 (não autorizado)
    
    def test_autenticacao_de_user_com_username_incorreto(self):
        """Teste que verifica a autenticacao de um user com o username incorreto"""
        user = authenticate(username='giovana', password='alura123') # cria um user com as credenciais corretas
        self.assertFalse((user is not None) and user.is_authenticated) # verifica se usuário não é nulo e se está autenticado

    def test_autenticacao_de_user_com_password_incorreto(self):
        """Teste que verifica a autenticacao de um user com o password incorreto"""
        user = authenticate(username='alura', password='1234567') # cria um user com as credenciais corretas
        self.assertFalse((user is not None) and user.is_authenticated) # verifica se usuário não é nulo e se está autenticado

    def test_requisicao_get_com_user_autenticado(self):
        """Teste que verifica uma requisição GET com user autenticado"""
        self.client.force_authenticate(user=self.user) # força a autenticação do user
        response = self.client.get(self.list_url) # faz uma requisição GET com autenticacao
        self.assertEqual(response.status_code, status.HTTP_200_OK) # verifica se o status code é 200 (ok)159357
        