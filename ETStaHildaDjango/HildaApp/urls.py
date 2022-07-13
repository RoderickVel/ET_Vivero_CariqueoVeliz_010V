from django.urls import path
from .views import form_crear_producto, form_mod_cliente, formulario_registro, index, somos, formulario, productos, mostrar_clientes, form_crear_cliente, mostrar_productos, form_crear_producto, form_mod_cliente, form_mod_producto,form_del_cliente,form_del_producto

urlpatterns = [
    path('', index, name="index"),
    path('productos/', productos, name="productos"),
    path('somos/', somos, name="somos"),
    path('formulario/', formulario, name="formulario"),
    path('formulario_registro/', formulario_registro, name="formulario_registro"),
    path('mostrar_clientes/', mostrar_clientes, name="mostrar_clientes"),
    path('form_crear_cliente/', form_crear_cliente, name="form_crear_cliente"),
    path('mostrar_productos/', mostrar_productos, name="mostrar_productos"),
    path('form_crear_producto/', form_crear_producto, name="form_crear_producto"),
    path('form_mod_producto/<id>', form_mod_producto, name="form_mod_producto"),
    path('form_mod_cliente/<id>', form_mod_cliente, name="form_mod_cliente"),
    path ('form_del_cliente/<id>', form_del_cliente, name="form_del_cliente"),
    path ('form_del_producto/<id>', form_del_producto, name="form_del_producto"),
]