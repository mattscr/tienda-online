from django.conf.urls import url #importamos las urls de django urls
from . import views #importamos los metodos de views.py
from django.urls import path, include, re_path
from .views import SignUpView, product_list
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'secciones'

urlpatterns = [
    
    

    path('register/', SignUpView.as_view(), name='register'),

    path('', product_list, name='home'),
    re_path(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),

]