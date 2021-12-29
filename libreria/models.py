from django.db import models

# Create your models here.
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100, verbose_name="nombre")
    apellidos=models.CharField(max_length=100)
    telefono=models.IntegerField()
    identificacion=models.CharField(max_length=100)
    staff=models.CharField(max_length=100)
    foto= models.ImageField(upload_to='imagenes/', null=True)

class Turnos(models.Model):
    id = models.AutoField(primary_key=True)
    numero = models.IntegerField()
    hora=models.TimeField()
    estado=models.CharField(max_length=100)
    Usuario=models.CharField(max_length=100)