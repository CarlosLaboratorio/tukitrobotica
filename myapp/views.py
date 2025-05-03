from django.shortcuts import render, redirect
from .models import Productos, Clientes, Vendedores, Comentario
from .forms import ProductoForm, ClienteForm, VendedorForm, ComentarioForm
from django.db.models import Q
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# Create your views here.

@login_required
def vista_privada(request):
    return render(request, 'myapp/vista_privada.html')

@login_required(login_url='login')
def index(request):
    contex = {"mensaje":"Bienvenidos a la página principal."}
    return render(request,"myapp/index.html",contex)

@login_required(login_url='login')
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

@login_required(login_url='login')
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm()
    return render(request, 'myapp/agregar_producto.html', {'form': form})

@login_required(login_url='login')
def lista_clientes(request):
    query = request.GET.get('q')
    if query:
        clientes = Clientes.objects.filter(nombre__icontains=query) | Clientes.objects.filter(apellido__icontains=query)| Clientes.objects.filter(email__icontains=query)
    else:
        clientes = Clientes.objects.all()
    return render(request, 'myapp/clientes.html', {'clientes': clientes})

@login_required(login_url='login')
def lista_vendedores(request):
    query = request.GET.get('q')
    if query:
        vendedores = Vendedores.objects.filter(nombre__icontains=query) | Vendedores.objects.filter(apellido__icontains=query)| Vendedores.objects.filter(email__icontains=query)
    else:
        vendedores = Vendedores.objects.all()
    return render(request, 'myapp/vendedores.html', {'vendedores': vendedores})

@login_required(login_url='login')
def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm()
    return render(request, 'myapp/agregar_cliente.html', {'form': form})

@login_required(login_url='login')
def agregar_vendedor(request):
    if request.method == 'POST':
        form = VendedorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vendedores')
    else:
        form = VendedorForm()
    return render(request, 'myapp/agregar_vendedor.html', {'form': form})

def acerca_de_mi(request):
    return render(request, 'myapp/acerca_de_mi.html', {})

class ProductoDetailView(DetailView):
    model = Productos
    template_name = 'myapp/detalle_productos.html'
    context_object_name = 'producto'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comentarios'] = self.object.comentarios.order_by('-fecha')
        context['form'] = ComentarioForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.producto = self.object
            comentario.save()
            return redirect('detalle_productos', pk=self.object.pk)
        return self.render_to_response(self.get_context_data(form=form))
    
class ProductoUpdateView(UpdateView):
    model = Productos
    template_name = 'myapp/editar_producto.html'
    fields = ['nombre', 'descripcion', 'precio', 'stock_total', 'categoria', 'imagen']
    success_url = reverse_lazy('productos')
    
class ProductoDeleteView(DeleteView):
    model = Productos
    template_name = 'myapp/eliminar_producto.html'
    success_url = reverse_lazy('productos')
    
def verificar_clave_vendedor(request, pk, accion):
    if request.method == 'POST':
        clave = request.POST.get('clave')
        if clave == 'admin123':
            request.session[f'clave_validada_vendedor_{pk}'] = True
            if accion == 'editar':
                return redirect('editar_vendedor', pk=pk)
            elif accion == 'eliminar':
                return redirect('eliminar_vendedor', pk=pk)
        else:
            messages.error(request, 'Clave incorrecta.')

    return render(request, 'myapp/verificar_clave.html', {'pk': pk, 'accion': accion})

class VendedorUpdateView(UpdateView,LoginRequiredMixin, TemplateView):
    model = Vendedores
    form_class = VendedorForm
    template_name = 'myapp/editar_vendedor.html'
    success_url = reverse_lazy('vendedores')
    
    def dispatch(self, request, *args, **kwargs):
        vendedor_id = self.kwargs['pk']
        if not request.session.get(f'clave_validada_vendedor_{vendedor_id}'):
            return redirect(reverse('verificar_clave_vendedor', args=[vendedor_id, 'editar']))
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        vendedor_id = self.kwargs['pk']
        if f'clave_validada_vendedor_{vendedor_id}' in self.request.session:
            del self.request.session[f'clave_validada_vendedor_{vendedor_id}']
        return super().form_valid(form)
    
class VendedorDeleteView(DeleteView, LoginRequiredMixin, TemplateView):
    model = Vendedores
    template_name = 'myapp/eliminar_vendedor.html'
    success_url = reverse_lazy('vendedores')

    def dispatch(self, request, *args, **kwargs):
        vendedor_id = self.kwargs['pk']
        if not request.session.get(f'clave_validada_vendedor_{vendedor_id}'):
            return redirect(reverse('verificar_clave_vendedor', args=[vendedor_id, 'eliminar']))
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        vendedor_id = self.kwargs['pk']
        if f'clave_validada_vendedor_{vendedor_id}' in self.request.session:
            del self.request.session[f'clave_validada_vendedor_{vendedor_id}']
        return super().form_valid(form)
    
class ClienteDeleteView(DeleteView):
    model = Clientes
    template_name = 'myapp/eliminar_cliente.html'
    success_url = reverse_lazy('clientes')
    
class ClienteUpdateView(UpdateView):
    model = Clientes
    form_class = ClienteForm
    template_name = 'myapp/editar_cliente.html'
    success_url = reverse_lazy('clientes')
    
class VistaProtegida(LoginRequiredMixin, TemplateView):
    template_name = 'myapp/protegida.html'