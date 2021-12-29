from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from .models import Turno
# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')
def usuarios(request):
    usuarios=Usuario.objects.all()
    return render(request,'usuarios/index.html',{'usuarios':usuarios})
def usuariosC(request):
    return render(request,'usuarios/crear.html')
def usuariosE(request):
    return render(request,'usuarios/editar.html')

def turnos(request):
    turnos=Turno.objects.all()
    return render(request,'turnos/index.html',{'turnos':turnos})
def turnosC(request):
    return render(request,'turnos/crear.html')
def turnosE(request):
    return render(request,'turnos/editar.html')