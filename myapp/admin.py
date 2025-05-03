from django.contrib import admin

from .models import Clientes, Vendedores, Productos, Categoria, Comentario

admin.site.register(Clientes)

admin.site.register(Vendedores)

admin.site.register(Productos)

admin.site.register(Categoria)

admin.site.register(Comentario)