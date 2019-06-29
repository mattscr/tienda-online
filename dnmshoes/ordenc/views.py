from django.shortcuts import render
from .models import OrdenItem
from .forms import FormCrearOrden
from carrito.carrito import Carrito


def crear_orden(request):
    carrito = Carrito(request)
    if request.method == 'POST':
        form = FormCrearOrden(request.POST)
        if form.is_valid():
            orden = form.save()
            for item in carrito:
                OrdenItem.objects.create(
                    orden=orden,
                    producto=item['producto'],
                    precio=item['precio'],
                    cantidad=item['cantidad']
                )
            carrito.limpiar()
        return render(request, 'ordenes/orden/creado.html', {'orden': orden})
    else:
        form = FormCrearOrden()
    return render(request, 'ordenes/orden/crear.html', {'form': form})