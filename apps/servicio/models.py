import time

from django.db import models

# Create your models here.
from django.urls import reverse

from bienes.funciones.validaciones_upload import validate_image_extension


class Persona(models.Model):
    # TIPO_PERSONA = (
    #     ('PA', 'Proveedor de Anuncios'),
    #     ('PN', 'Proveedor de Negocio'),
    #     ('CD', 'Cliente Directo'),
    #     ('CP', 'Cliente Propio')
    # )
    telefono = models.CharField(max_length=9)
    correo = models.EmailField(max_length=200)
    nombre_completo = models.CharField(max_length=200)

    # tipo_persona = models.CharField(max_length=2, choices=TIPO_PERSONA)

    def __str__(self):
        return "%s" % (self.nombre_completo)

    def get_absolute_url(self):
        return reverse('personal-success', kwargs={'pk': self.pk})


class Servicio(models.Model):
    TIPO_INMUEBLE = (
        ('TE', 'Terreno'),
        ('DE', 'Departamento'),
        ('CA', 'Casa')
    )
    ESTADO = (
        ('0', 'Vendido'),
        ('1', 'Pendiente')
    )
    PRIORIDAD = (
        ('0', 'Alto'),
        ('1', 'Medio'),
        ('2', 'Bajo')
    )
    nombre = models.CharField(max_length=500)
    descripcion = models.TextField()
    tipo_inmueble = models.CharField(max_length=2, choices=TIPO_INMUEBLE)
    estado = models.CharField(max_length=1, choices=ESTADO, default="1")
    inscrito_registro_publico = models.BooleanField(default=True)
    acabados = models.BooleanField(default=True)
    proveedor = models.ForeignKey('Persona', related_name='+', on_delete=models.CASCADE)
    monto_venta = models.DecimalField(max_digits=14, decimal_places=2)
    monto_vendido = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cliente = models.ForeignKey('Persona', blank=True, null=True, on_delete=models.CASCADE)
    fpublicacion = models.DateTimeField(auto_now_add=True)
    fventa = models.DateField(blank=True, null=True)
    proyeccion = models.TextField(blank=True, null=True)
    prioridad = models.CharField(max_length=1, choices=PRIORIDAD, blank=True, null=True)

    def __str__(self):
        return "%s" % (self.nombre)

    def get_absolute_url(self):
        return reverse('servicio-success', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-id']


class Comentario(models.Model):
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.texto)

    def get_absolute_url(self):
        return reverse('comentario-success', kwargs={'pk': self.pk})


class Video(models.Model):
    titulo = models.CharField(max_length=300)
    url = models.URLField()
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.url)

    def get_absolute_url(self):
        return reverse('videos-success', kwargs={'pk': self.pk})


def foto_directorio_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.id, ext)
    return '/'.join(['servicio', 'foto', time.strftime("%Y", time.gmtime()), time.strftime("%m", time.gmtime()),
                     time.strftime("%d", time.gmtime()), filename])


class Foto(models.Model):
    imagen = models.ImageField(upload_to=foto_directorio_path, validators=[validate_image_extension])
    orden = models.SmallIntegerField()
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)

    def __str__(self):
        return "Imagen %s" % (self.servicio)

    def get_absolute_url(self):
        return reverse('fotos-success', kwargs={'pk': self.pk})


class PuntoGeografico(models.Model):
    latitud = models.FloatField()
    longitud = models.FloatField()
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)

    def __str__(self):
        return "punto %s" % (self.servicio.nombre)

    def get_absolute_url(self):
        return reverse('punto_geografico-success', kwargs={'pk': self.pk})


class Dimension(models.Model):
    TIPO = (
        ('ANCHO', 'Ancho'),
        ('LARGO', 'Largo')
    )
    dimenciones = models.DecimalField(max_digits=8, decimal_places=2)
    tipo = models.CharField(max_length=5, choices=TIPO)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)

    def __str__(self):
        return "Dimension %s %s" % (self.tipo, self.dimenciones)

    def get_absolute_url(self):
        return reverse('dimensiones-success', kwargs={'pk': self.pk})
