"""dnmshoes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
#from jet.dashboard.dashboard_modules import google_analytics_views

admin.autodiscover()

urlpatterns = [
    #panel de administracion jet
	path('jet/', include('jet.urls', 'jet')),
	path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),

    #allauth (cuentas - sesiones - registro)
    path('accounts/', include('allauth.urls')),

    #carrito de compras 
    path('carrito/', include('carrito.urls')),

    #orden de compras
    path('ordenes/', include('orden.urls')),

    #principal
    path('', include('secciones.urls')),
 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)