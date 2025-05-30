from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone  # ← ESTA LÍNEA ES NECESARIA

class Carro(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio_por_dia = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='carros/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    estatus = models.CharField(max_length=50, default='pendiente')

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='items', on_delete=models.CASCADE)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateTimeField(default=timezone.now)  # ← YA FUNCIONA

class Carrito(models.Model):
    cliente = models.OneToOneField(User, on_delete=models.CASCADE)

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, related_name='items', on_delete=models.CASCADE)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
