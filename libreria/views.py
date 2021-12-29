from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')
def usuarios(request):
    return render(request,'usuarios/index.html')
def usuariosC(request):
    return render(request,'usuarios/crear.html')
def usuariosE(request):
    return render(request,'usuarios/editar.html')