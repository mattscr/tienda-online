from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from secciones.models import Producto
from .carrito import Carrito
from .forms import FormAgregarProductoCarrito


@require_POST
def carro_agregar(request, product_id):
    carro = Carrito(request)
    product = get_object_or_404(Producto, id_producto=product_id)
    form = FormAgregarProductoCarrito(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        carro.agregar(Producto=product, cantidad=cd['cantidad'], actualizar_cantidad=cd['actualizar'])
    return redirect('carrito:carrito_detalle')


def carro_remover(request, product_id):
    carro = Carrito(request)
    producto = get_object_or_404(Producto, id_producto=product_id)
    carro.remover(producto)
    return redirect('carrito:carrito_detalle')


def carro_detalle(request):
    carro = Carrito(request)
    for item in carro:
        item['form_actualizar_cantidad'] = FormAgregarProductoCarrito(initial={'cantidad': item['cantidad'], 'actualizar': True})
    return render(request, 'carrito/detalle.html', {'carrito': carro})