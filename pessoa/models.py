from django.db import models
from pessoa.validators import validate_cpf
from core.constants import UF
from core.models import Endereco

class Pessoa(models.Model):
    nome = models.CharField('nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11, validators=[validate_cpf], unique=True)
    email = models.EmailField('e-mail', unique=True)
    telefone = models.CharField(max_length=20)
    pagou = models.BooleanField(default=False)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    data_cadastro = models.DateTimeField('criado em', auto_now_add=True)


    class Meta:
        db_table = 'pessoa'
        verbose_name_plural = 'pessoas'
        verbose_name = 'pessoa'
        ordering = ('-data_cadastro',)

    def __str__(self):
        return self.nome
