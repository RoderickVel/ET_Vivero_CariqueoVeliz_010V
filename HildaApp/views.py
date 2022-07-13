from django.shortcuts import render, redirect
from django.views.decorators import csrf
from .models import Cliente, Producto
from .forms import ClienteForm, ProductoForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def productos(request):
    return render(request, 'productos.html')

def somos(request):
    return render(request, 'somos.html')

def formulario(request):
    return render(request, 'formulario.html')

def formulario_registro(request):
    return render(request, 'formulario_registro.html')

def mostrar_clientes(request):
    cliente = Cliente.objects.all()
    datos = {
        'cliente' : cliente
    }
    return render(request, 'mostrar_clientes.html', datos)

def mostrar_productos(request):
    producto = Producto.objects.all()
    datos = {
        'producto' : producto
    }
    return render(request, 'mostrar_productos.html', datos)

def form_crear_cliente(request):
    if request.method=='POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()        #similar al insert
            return redirect('mostrar_clientes')
    else:
        cliente_form=ClienteForm()
    return render(request, 'form_crear_cliente.html', {'cliente_form': cliente_form})

def form_crear_producto(request):
    if request.method=='POST':
        producto_form = ProductoForm(request.POST, request.FILES)
        if producto_form.is_valid():
            producto_form.save() #similar al insert
            return redirect('mostrar_productos')
    else:
        producto_form=ProductoForm()
    return render(request, 'form_crear_producto.html', {'producto_form': producto_form})

def form_mod_cliente(request, id):
    cliente =Cliente.objects.get(rut=id)
    datos = {
        'form': ClienteForm(instance = cliente)
    }
    if request.method=='POST':
        formulario = ClienteForm(data=request.POST, instance = cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect('mostrar_clientes')
    return render(request, 'form_mod_cliente.html', datos)

def form_mod_producto(request, id):
    producto =Producto.objects.get(id=id)
    datos = {
        'form': ProductoForm(instance = producto)
    }
    if request.method=='POST':
        formulario = ProductoForm(data=request.POST, instance = producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('mostrar_productos')
    return render(request, 'form_mod_producto.html', datos)

def form_del_cliente(request, id):
    cliente = Cliente.objects.get(rut=id)
    cliente.delete()
    return redirect('mostrar_clientes')

def form_del_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('mostrar_productos')