from django.contrib import admin

# Register your models here.
from .models import Contactos, Nosotros, Principal


class ContactosAdmin(admin.ModelAdmin):
    fields = ('imagen', 'titulo', 'direccion', 'telefono', 'email', 'estado')
    list_display = ('imagen', 'titulo', 'direccion', 'telefono', 'email', 'estado')


admin.site.register(Contactos, ContactosAdmin)


class NosotrosAdmin(admin.ModelAdmin):
    fields = ('imagen', 'titulo', 'subtitulo', 'descripcion', 'estado')
    list_display = ('imagen', 'titulo', 'subtitulo', 'descripcion', 'estado')


admin.site.register(Nosotros, NosotrosAdmin)


class PrincipalAdmin(admin.ModelAdmin):
    fields = ('imagen', 'titulo', 'subtitulo', 'descripcion', 'estado')
    list_display = ('imagen', 'titulo', 'subtitulo', 'descripcion', 'estado')


admin.site.register(Principal, PrincipalAdmin)
