from django.contrib import admin
from .models import Tenant


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ["name", "subdomain_prefix", "on_trial", ]
    search_fields = ['name',]