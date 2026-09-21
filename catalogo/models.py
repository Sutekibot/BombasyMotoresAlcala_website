import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    paternal_last_name = models.CharField(max_length=100, verbose_name='Apellido Paterno')
    maternal_last_name = models.CharField(max_length=100, verbose_name='Apellido Materno')

class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, verbose_name='Nombre de la Ubicación')
    location_type = models.CharField(max_length=100, verbose_name='Tipo de ubicación')
    
    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True, verbose_name='Nombre')
    code = models.CharField(max_length=50, unique=True, verbose_name='Código')
    product_type = models.CharField(max_length=100, verbose_name='Tipo')
    classification = models.CharField(max_length=100, verbose_name='Clasificación')
    is_active = models.BooleanField(default=True, verbose_name='Estatus')

    weight = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, verbose_name='Peso')
    height = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, verbose_name='Altura')
    width = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, verbose_name='Ancho')
    length = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, verbose_name='Largo')

    material = models.CharField(max_length=100, verbose_name='Material')
    color = models.CharField(max_length=50, verbose_name='Color')
    
    description = models.TextField(verbose_name='Descripción del Producto')
    locations = models.ManyToManyField(Location, through='LocationInventory', verbose_name='Ubicaciones')

    @property
    def stock_total(self):
        total = self.locationinventory_set.aggregate(total=models.Sum('stock'))['total']
        return total if total is not None else 0
    
    def __str__(self):
        return f"{self.code} - {self.name}"

class LocationInventory(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name='Ubicación')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Producto')
    stock = models.IntegerField(default=0, verbose_name='Existencia')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')

    class Meta:
        unique_together = ('location', 'product')
        verbose_name = 'Inventario por Ubicación'
        verbose_name_plural = 'Inventarios por Ubicación'
        
    def __str__(self):
        return f"{self.product.name} - {self.location.name} (Stock: {self.stock})"