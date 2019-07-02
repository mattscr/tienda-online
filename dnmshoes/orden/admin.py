from django.contrib import admin
from .models import Orden, OrdenItem


class OrdenItemInline(admin.TabularInline):
    model = OrdenItem
    raw_id_fields = ['producto']


class OrdenAdmin(admin.ModelAdmin):
    list_display = ['id', 'Nombre', 'Apellido', 'email', 'Direccion', 'Codigo_Postal', 'Ciudad', 'Pago', 'Creado',
                    'Actualizado']
    list_filter = ['Pago', 'Creado', 'Actualizado']
    inlines = [OrdenItemInline]


admin.site.register(Orden, OrdenAdmin)
