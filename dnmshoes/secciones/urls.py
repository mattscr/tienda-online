from django.conf.urls import url #importamos las urls de django urls
from . import views #importamos los metodos de views.py
from .views import SignUpView
from django.urls import path

app_name = 'secciones'

urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]