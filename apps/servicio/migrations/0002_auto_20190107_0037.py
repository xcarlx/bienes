# Generated by Django 2.1.4 on 2019-01-07 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='tipo_persona',
            field=models.CharField(choices=[('PA', 'Proveedor de Anuncios'), ('PN', 'Proveedor de Negocio'), ('CD', 'Cliente Directo'), ('CP', 'Cliente Propio')], max_length=1),
        ),
    ]
