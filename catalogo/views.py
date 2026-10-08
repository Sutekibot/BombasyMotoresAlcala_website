from django.shortcuts import render, get_object_or_404
from .models import Product, LocationInventory, ProductImage 
from django.db.models import Q

def inicio(request):
    return render(request, 'catalogo/inicio.html')

def lista_productos(request):
    producto = Product.objects.all()
    query = request.GET.get('q')
    filtrer_category = request.GET.get('category')
    filtrer_manufacturer = request.GET.get('manufacturer')
    if query:
        producto = producto.filter(
            Q(name__icontains=query) |
            Q(model__icontains=query) |
            Q(product_type__icontains=query) |
            Q(manufacturer__icontains=query) |
            Q(material__icontains=query) |
            Q(color__icontains=query) |
            Q(description__icontains=query)
        )
    if filtrer_category:
        producto = producto.filter(category=filtrer_category)
    if filtrer_manufacturer:
        producto = producto.filter(manufacturer=filtrer_manufacturer)
    marcas_unicas = Product.objects.values_list('manufacturer', flat=True).distinct()
    return render(request, 'catalogo/lista_productos.html', {'productos': producto, 'manufacturers': marcas_unicas})

def producto(request, producto_id):
    producto = get_object_or_404(Product, id=producto_id)
    inventario = LocationInventory.objects.filter(product=producto)
    imagenes_extra = ProductImage.objects.filter(product=producto)
    
    return render(request, 'catalogo/producto.html', {
        'producto': producto,
        'inventario': inventario,
        'imagenes_extra': imagenes_extra
    })