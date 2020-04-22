from django.conf.urls import url #importamos las urls de django urls
from . import views #importamos los metodos de views.py
from django.urls import path, re_path

app_name = 'secciones'

urlpatterns = [
    path('', views.product_list, name='home'),
    re_path(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]