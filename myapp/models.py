from django.db import models
from django.utils import timezone

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Vendedores(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.email}"

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.FloatField()
    stock_total = models.IntegerField()
    imagen = models.ImageField(upload_to='myapp/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Ventas(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedores, on_delete=models.CASCADE)
    fecha = models.DateField()
    total = models.FloatField()

    def __str__(self):
        return f"Venta #{self.id} - {self.fecha}"

class Detalle_Ventas(models.Model):
    venta = models.ForeignKey(Ventas, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.FloatField()
    subtotal = models.FloatField()

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"

class Stock(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE, related_name='movimientos_stock')
    cantidad = models.IntegerField()
    fecha_actualizacion = models.DateField()

    def __str__(self):
        return f"{self.producto.nombre} - {self.cantidad}"
    
class Comentario(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE, related_name='comentarios')
    nombre = models.CharField(max_length=100)
    texto = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comentario de {self.nombre} sobre {self.producto.nombre}'