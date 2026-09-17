import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

AUTH_USER_MODEL = 'catalogo.User'

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    paternal_last_name = models.CharField(max_length=100, verbosename='Apellido Paterno')
    maternal_last_name = models.CharField(max_length=100, verbosename='Apellido Materno')

class location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, verbosename='Nombre de la Ubicación')
    location_type = models.CharField(max_length=100, verbosename='Tipo de ubicación')
    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, verbosename='Nombre')
    code = models.CharField(max_length=50, verbosename='Código')
    total_stock = models.IntegerField(default=0,verbosename='Existencia')
    product_type = models.CharField(max_length=100, verbosename='Tipo')
    classification = models.CharField(max_length=100, verbosename='Clasificación')
    is_active = models.BooleanField(default=True, verbosename='Estatus')

    weight = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True, verbosename='Peso')
    height = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True, verbosename='Altura')
    width = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True, verbosename='Ancho')
    length = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True, verbosename='Largo')

    material = models.CharField(max_length=100, verbosename='Material')
    color = models.CharField(max_length=50, verbosename='Color')
    
    description = models.TextField(verbosename='Descripción del Producto')
    location = models.ManyToManyField(location, through='LocationInventory', verbosename='Ubicaciones')

    def __str__(self):
        return f"{self.code} - {self.name}"

class LocationInventory(models.Model):
    location = models.ForeignKey(location, on_delete=models.CASCADE, verbose_name='Ubicación')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Producto')
    stock = models.IntegerField(default=0, verbosename='Existencia')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbosename='Precio')

    class Meta:
        unique_together = ('location', 'product')
        verbose_name = 'Inventario por Ubicación'
        verbose_name_plural = 'Inventarios por Ubicación'
    def __str__(self):
        return f"{self.product.name} - {self.location.name} (Stock: {self.stock})"