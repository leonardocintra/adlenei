from django.db import models

class Arma(models.Model):
    descricao = models.CharField('descrição', max_length=100)
    marca = models.CharField(max_length=100)
    calibre = models.CharField(max_length=5)
    data_cadastro = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        db_table = 'arma'
        verbose_name_plural = 'armas'
        verbose_name = 'arma'
        ordering = ('-data_cadastro',)

    def __str__(self):
        return self.descricao
