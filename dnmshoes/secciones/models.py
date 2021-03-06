from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.safestring import mark_safe

# Create your models here.
class Slide(models.Model):
    caption1 = models.CharField(max_length=100)
    caption2 = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    imagen = models.ImageField(help_text="Size: 1920x570")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{} - {}".format(self.caption1, self.caption2)


class Marca (models.Model):
    id_marca = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Img_marca = models.ImageField(upload_to='img_marca', blank=True)

    def __str__(self):
        return self.Nombre


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=15)
    Slug = models.SlugField(max_length=150, unique=True,
                            default=str, db_index=True)
    Img_categoria = models.ImageField(upload_to='img_categoria', blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('Nombre', )
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.Nombre

    def get_absolute_url(self):
        return reverse('secciones:product_list_by_category', args=[self.Slug])


class Modelo(models.Model):
    id_modelo = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=20)
    Marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nombre


class CategoriaModelo(models.Model):
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    id_modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.id_categoria, self.id_modelo)


class Provincia(models.Model):
    id_provincia = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.Nombre


class Localidad(models.Model):
    id_localidad = models.AutoField(primary_key=True)
    Provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=20)

    class Meta:
        ordering = ('Nombre', )
        verbose_name = 'Localidad'
        verbose_name_plural = 'Localidades'

    def __str__(self):
        return self.Nombre


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    Modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    Color = models.CharField(max_length=10)
    Talle = models.CharField(max_length=4)
    Precio_Lista = models.CharField(max_length=10)
    Porcentaje_Ganancia = models.CharField(max_length=10)
    Total = models.CharField(max_length=6)
    Stock = models.CharField(max_length=3)
    Descripcion = models.CharField(max_length=101)
    slug = models.SlugField(max_length=150, default=str, db_index=True)
    disponibilidad = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to='img_productos/%Y/%m/%d', blank=True)

    def img_tag(self):
        if self.imagen:
            return mark_safe('<img src="%s" style="width: 45px; height:auto;" />' % self.imagen.url)
        else:
            return 'Imagen no encontrada'
    img_tag.short_description = 'Imagen'

    class Meta:
        ordering = ('Modelo', )
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    """ def __str__(self):      
        return ¿? """

    def get_absolute_url(self):
        return reverse('secciones:product_detail', args=[self.id_producto, self.slug])


class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    CUIT = models.CharField(max_length=11)
    Razon_social = models.CharField(max_length=30)
    CBU = models.CharField(max_length=20)
    Email = models.EmailField()
    Direccion = models.CharField(max_length=50)
    Localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    Telefono = models.CharField(max_length=15)

    class Meta:
        ordering = ('Razon_social', )
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return self.Razon_social


class ProductoProveedor(models.Model):
    Proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Precio_costo = models.CharField(max_length=5)
    Fecha = models.DateTimeField()


class MedioEnvio(models.Model):
    id_medioenvio = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=15)
    Tipo = models.CharField(max_length=15)


class Envio(models.Model):
    id_envio = models.AutoField(primary_key=True)
    Medio_de_envio = models.ForeignKey(MedioEnvio, on_delete=models.CASCADE)
    Direccion_de_envio = models.CharField(max_length=50)


class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    DNI = models.CharField(max_length=10)
    Forma_de_pago = models.CharField(max_length=10)


class Compra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    Usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    Envio = models.ForeignKey(Envio, on_delete=models.CASCADE)


class NotadePedido(models.Model):
    id_notadepedido = models.AutoField(primary_key=True)
    Fecha = models.DateField()
    Hora = models.TimeField()
    Usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    Estado = models.CharField(max_length=20)


class DetalleCompra(object):
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Nro_Nota_de_pedido = models.ForeignKey(
        NotadePedido, on_delete=models.CASCADE)
    Cantidad = models.CharField(max_length=5)


class Favorito(models.Model):
    id_favorito = models.AutoField(primary_key=True)
    Usuario = models.OneToOneField(User, on_delete=models.CASCADE)


class ProductoFavorito(models.Model):
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Favorito = models.ForeignKey(Favorito, on_delete=models.CASCADE)
