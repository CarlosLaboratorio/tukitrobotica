from django.db import models

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

class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    id_categoria = models.IntegerField()
    precio = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Ventas(models.Model):
    id_venta = models.IntegerField()
    id_cliente = models.IntegerField()
    id_vendedor = models.IntegerField()
    fecha = models.DateField()
    total = models.FloatField()

    def __str__(self):
        return self.nombre
    
class Detalle_Ventas(models.Model):
    id_detalle = models.IntegerField()
    id_venta = models.IntegerField()
    id_producto = models.IntegerField()
    cantidad = models.IntegerField()
    precio_unitario = models.FloatField()
    subtotal = models.FloatField()

    def __str__(self):
        return self.cantidad

class Stock(models.Model):
    id_producto = models.IntegerField()
    cantidad = models.IntegerField()
    fecha_actualizacion = models.DateField()
   

    def __str__(self):
        return self.nombre