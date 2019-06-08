from django.contrib import admin
from .models import Marca, Categoria, Modelo, CategoriaModelo, Provincia, Localidad, Producto, Proveedor, ProductoProveedor, MedioEnvio, Envio, Pago, Compra, NotadePedido

admin.site.site_header = "BENJAMIN Indumentaria"
admin.site.site_title  = "Panel de administración"
admin.site.index_title = "B E N J A M I N"


admin.site.register(Marca)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['Nombre', 'Slug']
    prepopulated_fields = {'Slug': ('Nombre',)}

admin.site.register(Categoria, CategoriaAdmin)

admin.site.register(Modelo)
#admin.site.register(CategoriaModelo)
admin.site.register(Provincia)
admin.site.register(Localidad)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['Modelo', 'Color', 'Stock', 'disponibilidad', 'Precio_Lista']
    list_filter = ['disponibilidad']
    list_editable = ['Precio_Lista', 'Stock', 'disponibilidad']
    prepopulated_fields = {'slug': ('Modelo',)}

admin.site.register(Producto, ProductoAdmin)

admin.site.register(Proveedor)
'''
admin.site.register(ProductoProveedor)
admin.site.register(MedioEnvio)
admin.site.register(Envio)
admin.site.register(Pago)
admin.site.register(Compra)
admin.site.register(NotadePedido)
'''