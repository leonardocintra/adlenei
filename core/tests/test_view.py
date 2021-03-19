from django.test import TestCase
from django.shortcuts import resolve_url as r
from django.db import IntegrityError
from django.test.client import Client
from django.contrib.auth.models import User

class IndexTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('core:index'))

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.response, 'index.html')
    
    def test_administrativo_link_usuario_nao_autenticado(self):
        with self.assertRaises(AssertionError):
            response = self.client.get(r('core:index'))
            expected = 'href="{}"'.format(r('core:administrativo')) 
            self.assertContains(response, expected)

    def test_administrativo_link_usuario_autenticado(self):
        self.client = Client()
        self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(r('core:index'))
        expected = 'href="{}"'.format(r('core:administrativo')) 
        self.assertContains(response, expected)
