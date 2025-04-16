from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='productos'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('clientes/', views.lista_clientes, name='clientes'),
    path('vendedores/', views.lista_vendedores, name='vendedores'),
]