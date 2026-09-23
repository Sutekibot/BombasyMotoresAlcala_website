from django.urls import path
from . import views
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('catalogo/', views.lista_productos, name='lista_productos'),
]

  