from django.conf.urls import url
from . import views

app_name = 'carrito'

urlpatterns = [
    url(r'^$', views.carro_detalle, name='carrito_detalle'),
    url(r'^add/(?P<product_id>\d+)/$', views.carro_agregar, name='carrito_agregar'),
    url(r'^remove/(?P<product_id>\d+)/$', views.carro_remover, name='carrito_remover'),
]