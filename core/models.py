from django.db import models
from pessoa.validators import validate_cnpj

class ClubeDeTiro(models.Model):
    nome = models.CharField('nome', max_length=100)
    cnpj = models.CharField('CPF', max_length=11, validators=[validate_cnpj], unique=True)
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
