# Generated by Django 2.1.4 on 2019-01-16 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0009_remove_persona_tipo_persona'),
    ]

    operations = [
        migrations.RenameField(
            model_name='puntogeografico',
            old_name='logitud',
            new_name='longitud',
        ),
    ]
