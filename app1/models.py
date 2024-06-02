from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)  # Renombrado y agregado max_length
    codigo = models.CharField(max_length=50)  # Agregado max_length
    proveedor = models.CharField(max_length=100)  # Corregida la ortografía y agregado max_length
    fecha = models.DateField()
    cantidad = models.IntegerField()
    precio_unidad = models.FloatField()  # Cambiado a snake_case
    precio_ganancias = models.FloatField()  # Cambiado a snake_case

    def __str__(self):
        return self.codigo

class Venta(models.Model):
    cantidad = models.IntegerField()
    fecha = models.DateField()
    hora = models.TimeField()
    precio = models.FloatField()
    descuento = models.FloatField()  # Cambiado a FloatField
    total = models.FloatField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  # Renombrado a minúsculas

    def __str__(self):
        return f'Venta {self.id} - Producto {self.producto.codigo}'
