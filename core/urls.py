from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('administrativo', views.administrativo, name='administrativo'),
    path('armas', views.armas, name='armas'),
    path('sobre', views.about, name='about'),
    path('contato', views.contact, name='contact'),
]