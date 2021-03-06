from django.db import models
from pessoa.validators import validate_cpf
from core.constants import UF


class EnderecoPessoa(models.Model):
    endereco = models.CharField('endereço', max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2, choices=UF)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, null=True, blank=True)
    cep = models.CharField(max_length=8)
    data_cadastro = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        db_table = 'endereco_pessoa'
        verbose_name_plural = 'enderecos da pessoa'
        verbose_name = 'endereco da pessoa'
        ordering = ('-data_cadastro',)

    def __str__(self):
        return self.endereco


class Pessoa(models.Model):
    nome = models.CharField('nome', max_length=100)
    endereco = models.ForeignKey(EnderecoPessoa, on_delete=models.CASCADE)
    cpf = models.CharField('CPF', max_length=11, validators=[
                           validate_cpf], unique=True)
    email = models.EmailField('e-mail', unique=True)
    telefone = models.CharField(max_length=20)
    pagou = models.BooleanField(default=False)
    data_cadastro = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        db_table = 'pessoa'
        verbose_name_plural = 'pessoas'
        verbose_name = 'pessoa'
        ordering = ('-data_cadastro',)

    def __str__(self):
        return self.nome
