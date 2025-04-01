
from django.shortcuts import render, get_object_or_404
from .models import Producto, Servicio

def lista_productos(request):
    producto = Producto.objects.all()
    return render(request, 'tienda/productos-list.html', {'producto': producto})

def detalle_producto(request, pk):
    producto = get_object_or_404(producto, pk=pk)
    return render(request, 'tienda/producto-detail.html', {'producto': producto})

def index(request):
    return render(request, 'tienda/index.html') 