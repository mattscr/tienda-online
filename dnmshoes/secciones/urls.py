from django.conf.urls import url #importamos las urls de django urls
from . import views #importamos los metodos de views.py
from django.urls import path, re_path
from .views import PrincipalView, TiendaView

app_name = 'secciones'

urlpatterns = [
    path('', PrincipalView.as_view(), name='home'),
    path('tienda/', TiendaView.as_view(), name='tienda'),
    #path('categoria/<slug>', CategoriaView.as_view(), name='product_list_by_category'),
    re_path(r'^(?P<category_slug>[-\w]+)/$', views.CategoriaFunc, name='product_list_by_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]