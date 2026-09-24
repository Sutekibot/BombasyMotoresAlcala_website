from django.shortcuts import render
from .models import Product

def inicio(request):
    return render(request, 'catalogo/inicio.html')

def lista_productos(request):
    producto = Product.objects.filter(is_active=True)
    return render(request, 'catalogo/lista_productos.html', {'productos': producto})
