import time

from django.db import models

# Create your models here.
from django.urls import reverse

from bienes.funciones.validaciones_upload import validate_image_extension


def principal_directorio_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.id, ext)
    return '/'.join(['home', 'principal', time.strftime("%Y", time.gmtime()), time.strftime("%m", time.gmtime()),
                     time.strftime("%d", time.gmtime()), filename])


class Principal(models.Model):
    imagen = models.ImageField(upload_to=principal_directorio_path, validators=[validate_image_extension])
    titulo = models.CharField(max_length=1000)
    subtitulo = models.CharField(max_length=1000)
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % (self.titulo)

    def get_absolute_url(self):
        return reverse('adm-success', kwargs={'pk': self.pk})


def nosotros_directorio_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.id, ext)
    return '/'.join(['home', 'nosotros', time.strftime("%Y", time.gmtime()), time.strftime("%m", time.gmtime()),
                     time.strftime("%d", time.gmtime()), filename])


class Nosotros(models.Model):
    imagen = models.ImageField(upload_to=nosotros_directorio_path, validators=[validate_image_extension])
    titulo = models.CharField(max_length=1000)
    subtitulo = models.CharField(max_length=1000)
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % (self.titulo)


def contactos_directorio_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.id, ext)
    return '/'.join(['home', 'contactos', time.strftime("%Y", time.gmtime()), time.strftime("%m", time.gmtime()),
                     time.strftime("%d", time.gmtime()), filename])


class Contactos(models.Model):
    imagen = models.ImageField(upload_to=contactos_directorio_path, validators=[validate_image_extension])
    titulo = models.CharField(max_length=1000)
    direccion = models.CharField(max_length=300)
    telefono = models.CharField(max_length=9)
    email = models.CharField(max_length=150)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return "%s || %s " % (self.titulo, self.telefono)
