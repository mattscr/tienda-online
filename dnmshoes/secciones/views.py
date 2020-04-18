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

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignUpForm

# Sign Up View
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('')
    template_name = 'secciones/register.html'

from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout

def login(request):
    # Creamos el formulario de autenticación vacío
    forml = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        forml = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if forml.is_valid():
            # Recuperamos las credenciales validadas
            username = forml.cleaned_data['username']
            password = forml.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "registration/login.html", {'forml': forml})

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')