from django.db import models


class Tenant(models.Model):
    name = models.CharField(max_length=100)
    subdomain_prefix = models.CharField(max_length=100, unique=True)
    on_trial = models.BooleanField('Versao de testes', default=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TenantAwareModel(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    class Meta:
        abstract = True
