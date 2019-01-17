from django.contrib import admin
from .models import Persona, Servicio, Comentario, Dimension, PuntoGeografico, Foto, Video


# Register your models here.


class PersonaAdmin(admin.ModelAdmin):
    fields = ('telefono', 'correo', 'nombre_completo')
    list_display = ('telefono', 'correo', 'nombre_completo')


admin.site.register(Persona, PersonaAdmin)


class ServicioAdmin(admin.ModelAdmin):
    fields = (
        'nombre', 'descripcion', 'tipo_inmueble', 'estado', 'inscrito_registro_publico', 'acabados', 'proveedor',
        'cliente', 'fventa', 'proyeccion', 'prioridad')

    list_display = (
        'nombre', 'descripcion', 'tipo_inmueble', 'estado', 'inscrito_registro_publico', 'acabados', 'proveedor',
        'cliente', 'fventa', 'proyeccion', 'prioridad')


admin.site.register(Servicio, ServicioAdmin)


class ComentarioAdmin(admin.ModelAdmin):
    fields = ('texto', 'fecha', 'servicio')
    list_display = ('texto', 'fecha', 'servicio')


admin.site.register(Comentario, ComentarioAdmin)


class DimensionAdmin(admin.ModelAdmin):
    fields = ('dimenciones', 'tipo', 'servicio')
    list_display = ('dimenciones', 'tipo', 'servicio')


admin.site.register(Dimension, DimensionAdmin)


class PuntoGeograficoAdmin(admin.ModelAdmin):
    fields = ('punto', 'servicio')
    list_display = ('punto', 'servicio')


admin.site.register(PuntoGeografico)


class FotoAdmin(admin.ModelAdmin):
    fields = ('imagen', 'servicio')
    list_display = ('imagen', 'servicio')


admin.site.register(Foto, FotoAdmin)


class VideoAdmin(admin.ModelAdmin):
    fields = ('url', 'servicio')
    list_display = ('url', 'servicio')


admin.site.register(Video, VideoAdmin)
