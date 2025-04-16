from django.shortcuts import render, redirect
from .models import Productos, Categoria, Clientes, Vendedores
from .forms import ProductoForm
from django.db.models import Q

# Create your views here.
def index(request):
    contex = {"mensaje":"Bienvenidos a la vista general de nuestros productos"}
    return render(request,"myapp/index.html",contex)

def lista_productos(request):
    query = request.GET.get('q')
    productos = Productos.objects.all()

    if query:
        productos = productos.filter(
            Q(nombre__icontains=query) |
            Q(descripcion__icontains=query) |
            Q(categoria__nombre__icontains=query)
        )

    return render(request, 'myapp/lista_productos.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm()
    return render(request, 'myapp/agregar_producto.html', {'form': form})

def lista_clientes(request):
    clientes = Clientes.objects.all()
    return render(request, 'myapp/clientes.html', {'clientes': clientes})

def lista_vendedores(request):
    vendedores = Vendedores.objects.all()
    return render(request, 'myapp/vendedores.html', {'vendedores': vendedores})