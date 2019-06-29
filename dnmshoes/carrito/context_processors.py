from .carrito import Carrito


def carro(request):
    return {'carrito': Carrito(request)}
