from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from comprovante.models import Arma

index = TemplateView.as_view(template_name='index.html')
about = TemplateView.as_view(template_name='about.html')
contact = TemplateView.as_view(template_name='contact.html')

administrativo = TemplateView.as_view(template_name='administrativo/principal.html')

armas = ListView.as_view(template_name='administrativo/arma_list.html', model=Arma)