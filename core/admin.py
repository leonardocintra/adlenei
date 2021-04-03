from django.contrib import admin
from core.models import ClubeDeTiro, EnderecoClube

class EnderecoClubeInline(admin.StackedInline):
    model = EnderecoClube
    extra = 1

class ClubeDeTiroAdmin(admin.ModelAdmin):
    inlines = [
        EnderecoClubeInline,
    ]

admin.site.register(ClubeDeTiro, ClubeDeTiroAdmin)