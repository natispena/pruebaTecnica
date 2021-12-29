from django.urls import path
from . import views

urlpatterns =[
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),

    
    path('usuarios', views.usuarios, name='usuarios'),
    path('usuarios/usuariosC', views.usuariosC, name='usuariosC'),
    path('usuarios/usuariosE',views.usuariosE, name='usuariosE'),

    
    path('turnos', views.turnos, name='turnos'),
    path('turnos/turnosC', views.turnosC, name='turnosC'),
    path('turnos/turnosE',views.turnosE, name='turnosE'),
]