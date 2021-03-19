from django.contrib import admin
from comprovante.models import Arma

class ArmaModelAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'marca', 'calibre']

admin.site.register(Arma, ArmaModelAdmin)
