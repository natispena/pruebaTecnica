from django.urls import path
from . import views

urlpatterns =[
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('usuarios', views.usuarios, name='usuarios'),
    path('usuarios/usuariosC', views.usuariosC, name='usuariosC'),
    path('usuarios/usuariosE',views.usuariosE, name='usuariosE'),
]