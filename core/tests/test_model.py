from django.test import TestCase

from pessoa.models import Pessoa
from core.models import ClubeDeTiro, EnderecoClube
from django.db import IntegrityError


class ClubeModelTest(TestCase):
    def setUp(self):
        self.clube = ClubeDeTiro.objects.create(
            nome='Team6',
            cnpj='63876989000111',
            email='teste@teste.com.br',
            telefone='168888484848',
        )

        self.endereco = EnderecoClube.objects.create(
            endereco='Rua 6 de abril',
            bairro='Centro',
            cidade='Ibiraci',
            uf='MG',
            numero='123',
            complemento='Perto do supermercado Hakime',
            cep='37990000',
            clube=self.clube
        )


    def test_create(self):
        self.assertTrue(ClubeDeTiro.objects.exists())

    def test_nome_is_not_blank(self):
        field = ClubeDeTiro._meta.get_field('nome')
        self.assertFalse(field.blank)

    def test_cnpj_is_not_blank(self):
        field = ClubeDeTiro._meta.get_field('cnpj')
        self.assertFalse(field.blank)

    def test_email_is_not_blank(self):
        field = ClubeDeTiro._meta.get_field('email')
        self.assertFalse(field.blank)

    def test_telefone_is_not_blank(self):
        field = ClubeDeTiro._meta.get_field('telefone')
        self.assertFalse(field.blank)


class EnderecoClubeModelTest(TestCase):
    def setUp(self):
        self.clube = ClubeDeTiro.objects.create(
            nome='Team6',
            cnpj='63876989000111',
            email='teste@teste.com.br',
            telefone='168888484848',
        )

        self.endereco = EnderecoClube.objects.create(
            endereco='Rua 6 de abril',
            bairro='Centro',
            cidade='Ibiraci',
            uf='MG',
            numero='123',
            complemento='Perto do supermercado Hakime',
            cep='37990000',
            clube=self.clube
        )

    def test_create(self):
        self.assertTrue(EnderecoClube.objects.exists())

    def test_endereco_is_not_blank(self):
        field = EnderecoClube._meta.get_field('endereco')
        self.assertFalse(field.blank)

    def test_bairro_is_not_blank(self):
        field = EnderecoClube._meta.get_field('bairro')
        self.assertFalse(field.blank)

    def test_cidade_is_not_blank(self):
        field = EnderecoClube._meta.get_field('cidade')
        self.assertFalse(field.blank)

    def test_uf_is_not_blank(self):
        field = EnderecoClube._meta.get_field('uf')
        self.assertFalse(field.blank)

    def test_numero_is_not_blank(self):
        field = EnderecoClube._meta.get_field('numero')
        self.assertFalse(field.blank)

    def test_complemento_is_blank(self):
        field = EnderecoClube._meta.get_field('complemento')
        self.assertTrue(field.blank)

    def test_cep_is_not_blank(self):
        field = EnderecoClube._meta.get_field('cep')
        self.assertFalse(field.blank)
