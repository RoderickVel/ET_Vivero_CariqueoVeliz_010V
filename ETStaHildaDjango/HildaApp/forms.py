from logging import PlaceHolder
from tkinter import DISABLED
from urllib import request
from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Cliente, Compra, Producto
from email.mime import image
from tkinter.tix import IMAGE
from random import randint

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
        fields = ['id', 'tipo', 'name', 'stock', 'price', 'image']
        labels ={
            'id': 'Id', 
            'tipo': 'Tipo', 
            'name': 'Nombre de Producto', 
            'price': 'Precio',
            'image' : 'Imagen',
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
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Nombre', 
                    'id': 'name'
                }
            ),

            'stock': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Stock', 
                    'id': 'stock'
                }
            ), 

            'price': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Precio',
                    'id': 'price',
                }
            ),

            'image': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Imagen',
                    'id': 'image',
                }
            )
        }

class CompraForm(forms.ModelForm):

    class Meta: 
        model= Compra
        fields = ['id_compra', 'total', 'estado']
        labels ={
            'id_compra': 'Id de compra', 
            'total': 'Total', 
            'estado': 'Estado Compra', 
        }
        widgets={
            'id_compra': forms.HiddenInput(
                attrs={
                    'class': 'form-control', 
                    'id': 'id_compra',
                    'editable': DISABLED,
                    'placeholder': randint(1,99999)
                }
            ), 
            'total': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Confirme total', 
                    'id': 'total'
                }
            ), 
            'estado': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese En Proceso', 
                    'id': 'estado'
                }
            )
        }