# Generated by Django 2.1.4 on 2019-01-28 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0003_auto_20190125_0332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='url',
        ),
        migrations.AddField(
            model_name='video',
            name='iframe',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
