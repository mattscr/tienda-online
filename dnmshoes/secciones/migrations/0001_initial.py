# Generated by Django 2.1.3 on 2018-11-12 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='CategoriaModelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secciones.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Envio',
            fields=[
                ('id_envio', models.AutoField(primary_key=True, serialize=False)),
                ('Direccion_de_envio', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id_localidad', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id_marca', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MedioEnvio',
            fields=[
                ('id_medioenvio', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=15)),
                ('Tipo', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id_modelo', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=20)),
                ('Marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secciones.Marca')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id_pago', models.AutoField(primary_key=True, serialize=False)),
                ('DNI', models.CharField(max_length=10)),
                ('Forma_de_pago', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('Color', models.CharField(max_length=10)),
                ('Talle', models.CharField(max_length=4)),
                ('Precio_Lista', models.CharField(max_length=10)),
                ('Porcentaje_Ganancia', models.CharField(max_length=10)),
                ('Total', models.CharField(max_length=6)),
                ('Stock', models.CharField(max_length=3)),
                ('Descripcion', models.CharField(max_length=101)),
                ('Categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secciones.Categoria')),
                ('Modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secciones.Modelo')),
            ],
        ),
        migrations.CreateModel(
            name='ProductoProveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Precio_costo', models.CharField(max_length=5)),
                ('Fecha', models.DateTimeField()),
                ('Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secciones.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_proveedor', models.AutoField(primary_key=True, serialize=False)),
                ('CUIT', models.CharField(max_length=11)),
                ('Razon_social', models.CharField(max_length=30)),
                ('CBU', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Direccion', models.CharField(max_length=50)),
                ('Telefono', models.CharField(max_length=15)),
                ('Localidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secciones.Localidad')),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id_provincia', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='productoproveedor',
            name='Proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secciones.Proveedor'),
        ),
        migrations.AddField(
            model_name='localidad',
            name='Provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secciones.Provincia'),
        ),
        migrations.AddField(
            model_name='envio',
            name='Medio_de_envio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secciones.MedioEnvio'),
        ),
        migrations.AddField(
            model_name='categoriamodelo',
            name='id_modelo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secciones.Modelo'),
        ),
    ]