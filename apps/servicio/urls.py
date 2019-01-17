"""bienes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .viewstotal import persona, servicio, comentario, punto_geografico, dimensiones, videos, fotos

urlpatterns = [
    path('personal/', persona.Home.as_view(), name='personal-principal'),
    path('personal/principal/data/', persona.ListaObject.as_view(), name='personal-data'),
    path('personal/agregar/', persona.CrearObjet.as_view(), name='personal-agregar'),
    path('personal/<int:pk>/editar/', persona.UpdateObject.as_view(), name='personal-editar'),
    path('personal/<int:pk>/eliminar/', persona.DeleteObject.as_view(), name='personal-eliminar'),
    path('personal/success/<int:pk>/', persona.SuccessObject.as_view(), name='personal-success'),

    path('servicio/', servicio.Home.as_view(), name='servicio-home'),
    path('servicio/principal/data/', servicio.ListaObject.as_view(), name='servicio-data'),
    path('servicio/agregar/', servicio.CrearObjet.as_view(), name='servicio-agregar'),
    path('servicio/<int:pk>/editar/', servicio.UpdateObject.as_view(), name='servicio-editar'),
    path('servicio/<int:pk>/eliminar/', servicio.DeleteObject.as_view(), name='servicio-eliminar'),
    path('servicio/success/<int:pk>/', servicio.SuccessObject.as_view(), name='servicio-success'),

    path('comentario/<int:servicio>/', comentario.Home.as_view(), name='comentario-home'),
    path('comentario/principal/<int:servicio>/data/', comentario.ListaObject.as_view(), name='comentario-data'),
    path('comentario/<int:servicio>/agregar/', comentario.CrearObjet.as_view(), name='comentario-agregar'),
    path('comentario/<int:pk>/editar/', comentario.UpdateObject.as_view(), name='comentario-editar'),
    path('comentario/<int:pk>/eliminar/', comentario.DeleteObject.as_view(), name='comentario-eliminar'),
    path('comentario/success/<int:pk>/', comentario.SuccessObject.as_view(), name='comentario-success'),

    path('punto_geografico/<int:servicio>/', punto_geografico.Home.as_view(), name='punto_geografico-home'),
    path('punto_geografico/principal/<int:servicio>/data/', punto_geografico.ListaObject.as_view(),
         name='punto_geografico-data'),
    path('punto_geografico/<int:servicio>/agregar/', punto_geografico.CrearObjet.as_view(),
         name='punto_geografico-agregar'),
    path('punto_geografico/<int:pk>/editar/', punto_geografico.UpdateObject.as_view(), name='punto_geografico-editar'),
    path('punto_geografico/<int:pk>/eliminar/', punto_geografico.DeleteObject.as_view(),
         name='punto_geografico-eliminar'),
    path('punto_geografico/success/<int:pk>/', punto_geografico.SuccessObject.as_view(),
         name='punto_geografico-success'),

    path('dimensiones/<int:servicio>/', dimensiones.Home.as_view(), name='dimensiones-home'),
    # path('dimensiones/principal/<int:servicio>/data/', dimensiones.ListaObject.as_view(), name='dimensiones-data'),
    path('dimensiones/<int:servicio>/agregar/', dimensiones.CrearObjet.as_view(), name='dimensiones-agregar'),
    path('dimensiones/<int:pk>/editar/', dimensiones.UpdateObject.as_view(), name='dimensiones-editar'),
    path('dimensiones/<int:pk>/eliminar/', dimensiones.DeleteObject.as_view(), name='dimensiones-eliminar'),
    path('dimensiones/success/<int:pk>/', dimensiones.SuccessObject.as_view(), name='dimensiones-success'),

    path('videos/<int:servicio>/', videos.Home.as_view(), name='videos-home'),
    # path('videos/principal/<int:servicio>/data/', videos.ListaObject.as_view(), name='videos-data'),
    path('videos/<int:servicio>/agregar/', videos.CrearObjet.as_view(), name='videos-agregar'),
    path('videos/<int:pk>/editar/', videos.UpdateObject.as_view(), name='videos-editar'),
    path('videos/<int:pk>/eliminar/', videos.DeleteObject.as_view(), name='videos-eliminar'),
    path('videos/success/<int:pk>/', videos.SuccessObject.as_view(), name='videos-success'),

    path('fotos/<int:servicio>/', fotos.Home.as_view(), name='fotos-home'),
    # path('fotos/principal/<int:servicio>/data/', fotos.ListaObject.as_view(), name='fotos-data'),
    path('fotos/<int:servicio>/agregar/', fotos.CrearObjet.as_view(), name='fotos-agregar'),
    path('fotos/<int:pk>/editar/', fotos.UpdateObject.as_view(), name='fotos-editar'),
    path('fotos/<int:pk>/eliminar/', fotos.DeleteObject.as_view(), name='fotos-eliminar'),
    path('fotos/success/<int:pk>/', fotos.SuccessObject.as_view(), name='fotos-success'),

]
