from django.db import models
from distutils.command.upload import upload
from django.forms import ImageField


# Create your models here.

class Cliente(models.Model):
    rut = models.CharField(max_length=9, primary_key=True, verbose_name='Rut')
    nombre= models.CharField(max_length=20, verbose_name='Nombre')
    direccion=models.CharField(max_length=20, verbose_name='Dirección')
    telefono=models.CharField(max_length=10, verbose_name='Telefono')
    edad=models.CharField(max_length=20, verbose_name='Edad')
    correo=models.CharField(max_length=50, verbose_name='Correo')

    def __str__(self):
        return self.rut

class Producto(models.Model):
    id = models.CharField(max_length=5, primary_key=True, verbose_name='Id')
    tipo= models.CharField(max_length=20, verbose_name='Tipo')
    nombreproducto=models.CharField(max_length=20, verbose_name='Nombre Producto')
    stock= models.CharField(max_length=20, verbose_name='Stock')
    precio=models.CharField(max_length=10, verbose_name='Precio')
    imagen=models.ImageField(upload_to="productos", null=True)
    def __str__(self):
        return self.nombreproducto