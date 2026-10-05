from django.shortcuts import render
from .models import Product
from django.db.models import Q

def inicio(request):
    return render(request, 'catalogo/inicio.html')

def lista_productos(request):
    producto = Product.objects.all()
    query = request.GET.get('q')
    filtrer_category = request.GET.get('category')
    if query:
        producto = producto.filter(
            Q(name__icontains=query) |
            Q(code__icontains=query) |
            Q(product_type__icontains=query) |
            Q(manufacturer__icontains=query) |
            Q(material__icontains=query) |
            Q(color__icontains=query) |
            Q(description__icontains=query)
        )
    if filtrer_category:
        producto = producto.filter(category=filtrer_category)
    return render(request, 'catalogo/lista_productos.html', {'productos': producto}) 
