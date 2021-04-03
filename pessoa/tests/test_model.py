from django.test import TestCase

from pessoa.models import Pessoa, EnderecoPessoa
from django.db import IntegrityError


class PessoaModelTest(TestCase):
    def setUp(self):
        self.endereco = EnderecoPessoa.objects.create(
            endereco='Rua 6 de abril',
            bairro='Centro',
            cidade='Ibiraci',
            uf='MG',
            numero='123',
            cep='37990000'
        )

        self.pessoa = Pessoa.objects.create(
            nome='Leonardo Nascimento Cintra',
            cpf='00022222222',
            email='leonardo@django.com.br',
            telefone='999999999',
            endereco=self.endereco
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
                nome='Outro Leonardo',
                cpf='00022222222',
                email='leonardddo@django.com.br',
                telefone='999999999',
                endereco=self.endereco
            )

    def test_create_same_email(self):
        with self.assertRaises(IntegrityError):
            Pessoa.objects.create(
                nome='Outro Leonardo',
                cpf='88888877765',
                email='leonardo@django.com.br',
                telefone='999999999',
                endereco=self.endereco
            )

    def test_pagou_default_to_False(self):
        """By default pagou must be False."""
        self.assertEqual(False, self.pessoa.pagou)

    def test_str(self):
        self.assertEqual('Leonardo Nascimento Cintra', str(self.pessoa))
