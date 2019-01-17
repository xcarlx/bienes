# Generated by Django 2.1.4 on 2019-01-07 04:37

import apps.servicio.models
import bienes.funciones.validaciones_upload
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0002_auto_20190107_0037'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dimension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dimenciones', models.DecimalField(decimal_places=2, max_digits=8)),
                ('tipo', models.CharField(choices=[('ANCHO', 'Ancho'), ('LARGO', 'Largo')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to=apps.servicio.models.foto_directorio_path, validators=[bienes.funciones.validaciones_upload.validate_image_extension])),
            ],
        ),
        migrations.CreateModel(
            name='PuntoGeografico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelogis', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500)),
                ('descripcion', models.TextField()),
                ('tipo_inmueble', models.CharField(choices=[('TE', 'Terreno'), ('DE', 'Departamento'), ('CA', 'Casa')], max_length=2)),
                ('estado', models.CharField(choices=[('0', 'Vendido'), ('1', 'Pendiente')], max_length=1)),
                ('inscrito_registro_publico', models.BooleanField(default=True)),
                ('acabados', models.BooleanField(default=True)),
                ('fpublicacion', models.DateTimeField(auto_now_add=True)),
                ('fventa', models.DateField(blank=True, null=True)),
                ('proyeccion', models.TextField(blank=True, null=True)),
                ('prioridad', models.CharField(blank=True, choices=[('0', 'Alto'), ('1', 'Medio'), ('2', 'Bajo')], max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicio.Servicio')),
            ],
        ),
        migrations.AlterField(
            model_name='persona',
            name='tipo_persona',
            field=models.CharField(choices=[('PA', 'Proveedor de Anuncios'), ('PN', 'Proveedor de Negocio'), ('CD', 'Cliente Directo'), ('CP', 'Cliente Propio')], max_length=2),
        ),
        migrations.AddField(
            model_name='servicio',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='servicio.Persona'),
        ),
        migrations.AddField(
            model_name='servicio',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='servicio.Persona'),
        ),
        migrations.AddField(
            model_name='puntogeografico',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicio.Servicio'),
        ),
        migrations.AddField(
            model_name='foto',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicio.Servicio'),
        ),
        migrations.AddField(
            model_name='dimension',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicio.Servicio'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicio.Servicio'),
        ),
    ]
