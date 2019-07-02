from django.conf.urls import url
from . import views

app_name = 'ordenes'

urlpatterns = [
    url(r'^crear/$', views.crear_orden, name='crear_orden')
]