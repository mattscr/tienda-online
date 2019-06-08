from decimal import Decimal
from django.conf import settings
from secciones.models import Producto


class Carrito(object):
    def __init__(self, request):
        self.session = request.session
        carro = self.session.get(settings.CART_SESSION_ID)
        if not carro:
            carro = self.session[settings.CART_SESSION_ID] = {}
        self.carro = carro

    def agregar(self, Producto, cantidad=1, actualizar_cantidad=False):
        producto_id = str(Producto.id_producto)
        if producto_id not in self.carro:
            self.carro[producto_id] = {'cantidad': 0, 'precio': str(Producto.Total)}
        if actualizar_cantidad:
            self.carro[producto_id]['cantidad'] = cantidad
        else:
            self.carro[producto_id]['cantidad'] += cantidad
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.carro
        self.session.modified = True

    def remover(self, Producto):
        producto_id = str(Producto.id_producto)
        if producto_id in self.carro:
            del self.carro[producto_id]
            self.save()

    def __iter__(self):
        producto_ids = self.carro.keys()
        productos = Producto.objects.filter(id_producto__in=producto_ids)
        print(productos)
        for producto in productos:
            self.carro[str(producto.id_producto)]['producto'] = producto
            print(Producto.id_producto)

        for item in self.carro.values():
            item['precio'] = Decimal(item['precio'])
            item['precio_total'] = item['precio'] * item['cantidad']
            yield item

    def __len__(self):
        return sum(item['cantidad'] for item in self.carro.values())

    def get_total_price(self):
        return sum(Decimal(item['precio']) * item['cantidad'] for item in self.carro.values())

    def limpiar(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True