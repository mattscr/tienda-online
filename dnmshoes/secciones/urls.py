from django.conf.urls import url #importamos las urls de django urls
from . import views #importamos los metodos de views.py
from .views import SignUpView, logout
from django.contrib.auth import views as auth_views

app_name = 'secciones'

urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    #path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 

    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]