from django.shortcuts import render, get_object_or_404
from .models import Categoria, Producto
from carrito.forms import FormAgregarProductoCarrito
from django.views.generic import ListView, DetailView, View

class HomeView (ListView):
    template_name = "index.html"
    queryset = Producto.objects.filter(disponibilidad=True)
    context_object_name = 'Productos'

class ShopView(ListView):
    model = Producto
    paginate_by = 6 
    template_name =  "productos/listado_productos.html"


def CategoriaFunc(request, category_slug=None):
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
    return render(request, 'productos/categoria.html', context)


def product_detail(request, id, slug):
    producto = get_object_or_404(Producto, id_producto=id, slug=slug, disponibilidad=True)
    form_carrito_producto = FormAgregarProductoCarrito()
    context = {
        'producto': producto,
        'form_carrito_producto': form_carrito_producto
    }
    return render(request, 'productos/detail.html', context)

