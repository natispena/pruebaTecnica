from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import  static

urlpatterns =[
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),

    
    path('usuarios', views.usuarios, name='usuarios'),
    path('usuarios/usuariosC', views.usuariosC, name='usuariosC'),
    path('usuarios/usuariosE',views.usuariosE, name='usuariosE'),
    path('usuariosB/<int:id>',views.usuariosB, name='usuariosB'),


    
    path('turnos', views.turnos, name='turnos'),
    path('turnos/turnosC', views.turnosC, name='turnosC'),
    path('turnos/turnosE',views.turnosE, name='turnosE'),
    path('turnosB/<int:id>',views.turnosB, name='turnosB'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)