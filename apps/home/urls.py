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
from .viewstotal import inicio, principal

urlpatterns = [
    path('', inicio.HomeTemplate.as_view(), name='home'),
    path('login/', inicio.Login.as_view(), name='login'),
    path('logout/', inicio.Logout.as_view(), name='logout'),

    path('administracion/', inicio.AdministracionTemplate.as_view(), name='home-administracion'),
    path('administracion/principal/', principal.Home.as_view(), name='adm-principal'),
    path('administracion/principal/data/', principal.ListaObject.as_view(), name='adm-data'),
    path('administracion/agregar/', principal.CrearObjet.as_view(), name='adm-agregar'),
    path('administracion/<int:pk>/editar/', principal.UpdateObject.as_view(), name='adm-editar'),
    path('administracion/<int:pk>/eliminar/', principal.DeleteObject.as_view(), name='adm-eliminar'),
    path('administracion/success/<int:pk>/', principal.SuccessObject.as_view(), name='adm-success'),

]
