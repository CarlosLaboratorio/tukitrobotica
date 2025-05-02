from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='productos'),
    path('agregarp/', views.agregar_producto, name='agregar_producto'),
    path('clientes/', views.lista_clientes, name='clientes'),
    path('vendedores/', views.lista_vendedores, name='vendedores'),
    path('agregarc/', views.agregar_cliente, name='agregar_cliente'),
    path('agregarv/', views.agregar_vendedor, name='agregar_vendedor'),
    path('acercade/', views.acerca_de_mi, name='acerca_de_mi'),
    path('detallepro/<int:pk>', views.ProductoDetailView.as_view() , name='detalle_productos'),
    path('editar_producto/<int:pk>/', views.ProductoUpdateView.as_view(), name='editar_producto'),
    path('eliminar_producto/<int:pk>/', views.ProductoDeleteView.as_view(), name='eliminar_producto'),
    path('verificar-clave-vendedor/<int:pk>/<str:accion>/', views.verificar_clave_vendedor, name='verificar_clave_vendedor'),
    path('editar_vendedor/<int:pk>/', views.VendedorUpdateView.as_view(), name='editar_vendedor'),
    path('eliminar_vendedor/<int:pk>/', views.VendedorDeleteView.as_view(), name='eliminar_vendedor'),
]