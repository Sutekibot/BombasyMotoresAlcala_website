from django.test import TestCase
from django.urls import reverse
from .models import Product
import uuid

class VistasCatalogoTests(TestCase):
    # 1. PREPARACIÓN: Django ejecuta esto antes de cada prueba
    def setUp(self):
        # Agregamos el campo "code" con valores únicos para que la base de datos lo acepte
        self.motor = Product.objects.create(
            code="MOT-001",
            name="Motor Siemens 5HP",
            model="1LA7",
            manufacturer="Siemens",
            category="Motor",
            is_active=True
        )
        self.bomba = Product.objects.create(
            code="BOM-001",
            name="Bomba de Agua Truper",
            model="BOM-1/2",
            manufacturer="Truper",
            category="Bomba",
            is_active=True
        )

    # 2. PRUEBA: ¿Carga bien el catálogo completo?
    def test_lista_productos_carga_bien(self):
        response = self.client.get(reverse('lista_productos'))
        self.assertEqual(response.status_code, 200) # 200 significa "OK"
        self.assertContains(response, "Motor Siemens 5HP")
        self.assertContains(response, "Bomba de Agua Truper")

    # 3. PRUEBA: ¿Funciona el buscador de la barra azul?
    def test_buscador_filtra_correctamente(self):
        # Simulamos buscar "Siemens"
        response = self.client.get(reverse('lista_productos') + '?q=Siemens')
        
        self.assertEqual(response.status_code, 200)
        # Debe aparecer el motor, pero la bomba NO debe aparecer
        self.assertContains(response, "Motor Siemens 5HP")
        self.assertNotContains(response, "Bomba de Agua Truper")

    # 4. PRUEBA: ¿Carga bien la página de detalles de un producto?
    def test_detalle_producto_carga_bien(self):
        # Usamos el UUID real del motor que creamos en el setUp
        url = reverse('detalle_producto', args=[self.motor.id])
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Siemens")
        self.assertContains(response, "1LA7")

    # 5. PRUEBA: ¿Qué pasa si alguien inventa una URL con un UUID falso?
    def test_detalle_producto_no_existente_da_404(self):
        uuid_falso = uuid.uuid4() # Generamos un UUID al azar
        url = reverse('detalle_producto', args=[uuid_falso])
        response = self.client.get(url)
        
        # Debe dar error 404 (Página no encontrada), no debe "romperse" el servidor (500)
        self.assertEqual(response.status_code, 404)