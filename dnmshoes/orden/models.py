from django.db import models
from secciones.models import Producto


class Orden(models.Model):
    Nombre = models.CharField(max_length=60)
    Apellido = models.CharField(max_length=60)
    email = models.EmailField()
    Direccion = models.CharField(max_length=150)
    Codigo_Postal = models.CharField(max_length=30)
    Ciudad = models.CharField(max_length=100)
    Creado = models.DateTimeField(auto_now_add=True)
    Actualizado = models.DateTimeField(auto_now=True)
    Pago = models.BooleanField(default=False)

    class Meta:
        ordering = ('-Creado', )
        verbose_name= 'Orden'
        verbose_name_plural = 'Ordenes'

    def __str__(self):
        return 'Orden {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrdenItem(models.Model):
    orden = models.ForeignKey(Orden, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, related_name='orden_items', on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.precio * self.cantidad