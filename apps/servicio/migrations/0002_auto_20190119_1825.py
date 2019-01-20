# Generated by Django 2.1.4 on 2019-01-19 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='monto_vendido',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True),
        ),
        migrations.AddField(
            model_name='servicio',
            name='monto_venta',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=14),
            preserve_default=False,
        ),
    ]
