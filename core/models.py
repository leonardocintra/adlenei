from django.db import models
from pessoa.validators import validate_cnpj
from core.constants import UF


class ClubeDeTiro(models.Model):
    nome = models.CharField('nome', max_length=100)
    cnpj = models.CharField('CNPJ', max_length=11, validators=[
                            validate_cnpj], unique=True)
    email = models.EmailField('e-mail', unique=True)
    telefone = models.CharField(max_length=20)
    data_cadastro = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        db_table = 'clube_de_tiro'
        verbose_name_plural = 'clubes de tiro'
        verbose_name = 'clube de tiro'
        ordering = ('-data_cadastro',)

    def __str__(self):
        return self.nome


class Endereco(models.Model):
    endereco = models.CharField('endereço', max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2, choices=UF)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, null=True)
    cep = models.CharField(max_length=8)
    data_cadastro = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        db_table = 'endereco'
        verbose_name_plural = 'endereços'
        verbose_name = 'endereco'
        ordering = ('-data_cadastro',)

    def __str__(self):
        return self.endereco


class ClubeEndereco(models.Model):
    clube = models.ForeignKey(ClubeDeTiro, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    data_cadastro = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        db_table = 'clube_endereco'
        verbose_name_plural = 'clube e endereços'
        verbose_name = 'clube endereco'
        ordering = ('-data_cadastro',)

    def __str__(self):
        return self.clube
