from django.db import models
from .choices import  estados,staff
from django.contrib.auth.models import  User
# Create your models here.


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100, verbose_name="nombre")
    apellidos=models.CharField(max_length=100)
    telefono=models.IntegerField()
    identificacion=models.CharField(max_length=100)
    staff=models.CharField(max_length=100, choices=staff , default='n')
    foto= models.ImageField(upload_to='imagenes/', null=True)
    
    def delete(self, using=None, keep_parents= False):
        self.imagenes.storage.delete(self.foto.mane)
        super().delete()

class Turno(models.Model):
    id = models.AutoField(primary_key=True)
    numero = models.IntegerField()
    hora=models.TimeField()
    estado=models.CharField(max_length=100, choices=estados, default='p')
    Usuario=models.ForeignKey(Usuario, null=True, on_delete=models.CASCADE)
    usuarioEditor= models.CharField(max_length=100, null=True)

