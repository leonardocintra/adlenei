from django.test import TestCase

from pessoa.models import Pessoa

class PessoaModelTest(TestCase):
    def setUp(self):
        self.pessoa = Pessoa.objects.create(
            nome = 'Leonardo Nascimento Cintra',
            cpf = '00022222222',
            email = 'leonardo@django.com.br',
            telefone = '999999999'
        )
    
    def test_create(self):
        self.assertTrue(Pessoa.objects.exists())

    def test_email_is_not_blank(self):
        field = Pessoa._meta.get_field('email')
        self.assertFalse(field.blank)

    def test_cpf_is_not_blank(self):
        field = Pessoa._meta.get_field('cpf')
        self.assertFalse(field.blank)
    
    def test_telefone_is_not_blank(self):
        field = Pessoa._meta.get_field('telefone')
        self.assertFalse(field.blank)

    def test_pagou_is_not_blank(self):
        field = Pessoa._meta.get_field('pagou')
        self.assertFalse(field.blank)
        
    def test_pagou_default_to_False(self):
        """By default pagou must be False."""
        self.assertEqual(False, self.pessoa.pagou)
    
    def test_str(self):
        self.assertEqual('Leonardo Nascimento Cintra', str(self.pessoa))

    