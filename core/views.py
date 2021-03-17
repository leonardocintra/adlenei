from django.shortcuts import render
from django.views.generic import TemplateView

index = TemplateView.as_view(template_name='index.html')

administrativo = TemplateView.as_view(template_name='administrativo/principal.html')