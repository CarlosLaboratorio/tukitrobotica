from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='productos'),
    path('agregarp/', views.agregar_producto, name='agregar_producto'),
    path('clientes/', views.lista_clientes, name='clientes'),
    path('vendedores/', views.lista_vendedores, name='vendedores'),
    path('agregarc/', views.agregar_cliente, name='agregar_cliente'),
    path('agregarv/', views.agregar_vendedor, name='agregar_vendedor'),
]