from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Cliente, Producto
from email.mime import image
from tkinter.tix import IMAGE

class ClienteForm(forms.ModelForm):

    class Meta: 
        model= Cliente
        fields = ['rut', 'nombre', 'direccion', 'telefono', 'edad', 'correo']
        labels ={
            'rut': 'Rut', 
            'nombre': 'Nombre', 
            'direccion': 'Dirección', 
            'telefono': 'Teléfono',
            'edad': 'Edad',
            'correo': 'Correo',
        }
        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'id': 'rut'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Nombre', 
                    'id': 'nombre'
                }
            ), 
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Dirección', 
                    'id': 'direccion'
                }
            ), 
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Teléfono',
                    'id': 'telefono',
                }
            ),
            'edad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Edad',
                    'id': 'edad',
                }
            ),
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Correo',
                    'id': 'correo',
                }
            )

        }

class ProductoForm(forms.ModelForm):

    class Meta: 
        model= Producto
        fields = ['id', 'tipo', 'nombreproducto', 'stock', 'precio', 'imagen']
        labels ={
            'id': 'Id', 
            'tipo': 'Tipo', 
            'nombreproducto': 'Nombre de Producto', 
            'precio': 'Precio',
            'imagen' : 'Imagen',
        }
        widgets={
            'id': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'id': 'id'
                }
            ), 
            'tipo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Tipo', 
                    'id': 'tipo'
                }
            ), 
            'nombreproducto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Nombre', 
                    'id': 'nombreproducto'
                }
            ),

            'stock': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Stock', 
                    'id': 'stock'
                }
            ), 

            'precio': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Precio',
                    'id': 'precio',
                }
            ),

            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Imagen',
                    'id': 'imagen',
                }
            )



        }