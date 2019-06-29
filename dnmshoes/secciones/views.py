from django.shortcuts import render, get_object_or_404
from .models import Categoria, Producto
from carrito.forms import FormAgregarProductoCarrito


def product_list(request, category_slug=None):
    categoria = None
    categorias = Categoria.objects.all()
    productos = Producto.objects.filter(disponibilidad=True)
    if category_slug:
        categoria = get_object_or_404(Categoria, Slug=category_slug)
        productos = Producto.objects.filter(Categoria=categoria)

    context = {
        'categoria': categoria,
        'categorias': categorias,
        'productos': productos
    }
    return render(request, 'secciones/productos/list.html', context)


def product_detail(request, id, slug):
    producto = get_object_or_404(Producto, id_producto=id, slug=slug, disponibilidad=True)
    form_carrito_producto = FormAgregarProductoCarrito()
    context = {
        'producto': producto,
        'form_carrito_producto': form_carrito_producto
    }
    return render(request, 'secciones/productos/detail.html', context)



  