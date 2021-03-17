from django.test import TestCase

from pessoa.models import Pessoa, Endereco
from django.db import IntegrityError

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

    def test_create_same_cpf(self):
        with self.assertRaises(IntegrityError):
            Pessoa.objects.create(
                nome = 'Outro Leonardo',
                cpf = '00022222222',
                email = 'leonardddo@django.com.br',
                telefone = '999999999'
            )

    def test_create_same_email(self):
        with self.assertRaises(IntegrityError):
            Pessoa.objects.create(
                nome = 'Outro Leonardo',
                cpf = '88888877765',
                email = 'leonardo@django.com.br',
                telefone = '999999999'
            )

    def test_pagou_default_to_False(self):
        """By default pagou must be False."""
        self.assertEqual(False, self.pessoa.pagou)
    
    def test_str(self):
        self.assertEqual('Leonardo Nascimento Cintra', str(self.pessoa))


class EnderecoModelTest(TestCase):
    def setUp(self):
        self.pessoa = Pessoa.objects.create(
            nome = 'Leonardo Nascimento Cintra',
            cpf = '00022222222',
            email = 'leonardo@django.com.br',
            telefone = '999999999'
        )

        self.endereco = Endereco.objects.create(
            pessoa = self.pessoa,
            endereco = 'Rua 6 de abril',
            bairro = 'Centro',
            cidade = 'Ibiraci',
            uf = 'MG',
            numero = '123',
            complemento = 'Perto do supermercado Hakime',
            cep = '37990000',
        )
    
    def test_create(self):
        self.assertTrue(Pessoa.objects.exists())
        self.assertTrue(Endereco.objects.exists())
    
    def test_endereco_is_not_blank(self):
        field = Endereco._meta.get_field('endereco')
        self.assertFalse(field.blank)
    
    def test_bairro_is_not_blank(self):
        field = Endereco._meta.get_field('bairro')
        self.assertFalse(field.blank)

    def test_cidade_is_not_blank(self):
        field = Endereco._meta.get_field('cidade')
        self.assertFalse(field.blank)

    def test_uf_is_not_blank(self):
        field = Endereco._meta.get_field('uf')
        self.assertFalse(field.blank)

    def test_numero_is_not_blank(self):
        field = Endereco._meta.get_field('numero')
        self.assertFalse(field.blank)

    def test_complemento_is_not_blank(self):
        field = Endereco._meta.get_field('complemento')
        self.assertFalse(field.blank)

    def test_cep_is_not_blank(self):
        field = Endereco._meta.get_field('cep')
        self.assertFalse(field.blank)