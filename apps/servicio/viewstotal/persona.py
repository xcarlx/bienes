from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.db.models import Q, ProtectedError
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView
from django.views.generic.base import View
from ..models import Persona as Object
from ..formstotal.persona import PersonalForm as Formulario


class Home(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    template_name = "servicio/personal/home.html"


class ListaObject(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        length = request.GET.get('length', None)
        search = request.GET.get('search[value]', None)
        draw = request.GET.get('draw', 1)
        order0 = request.GET.get('order[0][dir]', "")
        start = request.GET.get('start', None)
        if length is None:
            length = 0
        if order0 is not None:
            if order0 == "asc":
                order0 = ''
            else:
                order0 = '-'
        if start is not None:
            start = (int(start) / int(length)) + 1

        if search is not None:
            objeto = Object.objects.filter(
                Q(nombre_completo__icontains=search)
            ).order_by(order0 + 'id')
            total = objeto.count()
            paginator = Paginator(objeto, length)

            obj = paginator.get_page(start)

            lista = list()
            for object in obj:
                dict = {
                    "id": object.id,
                    "telefono": object.telefono,
                    "correo": object.correo,
                    "nombre_completo": object.nombre_completo,
                }
                lista.append(dict)
            object = {
                "draw": draw,
                "recordsTotal": total,
                "recordsFiltered": total,
                "data": lista
            }
            return JsonResponse(object)
        return JsonResponse({})


class SuccessObject(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        if int(kwargs.get('pk')) == 0:
            objecdic = {
                "mensaje": "Eliminado Correctamente",
                "datos": {
                    "descripcion": ""
                }
            }
        else:
            objeto = Object.objects.get(pk=kwargs.get('pk'))
            objecdic = {
                "mensaje": "Guardado Correctamente",
                "datos": {
                    "descripcion": objeto.nombre_completo
                }
            }
        return JsonResponse(objecdic)


class CrearObjet(LoginRequiredMixin, CreateView):
    login_url = 'login'
    form_class = Formulario
    template_name = "servicio/personal/formulario.html"

    def form_valid(self, form):
        # form.instance.creador = self.request.user
        return super(CrearObjet, self).form_valid(form)


class UpdateObject(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Object
    form_class = Formulario
    template_name = "servicio/personal/formulario.html"

    def form_valid(self, form):
        # form.instance.editor = self.request.user
        return super(UpdateObject, self).form_valid(form)


class DeleteObject(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = Object
    template_name = "servicio/personal/delete_form.html"
    success_url = None

    def delete(self, request, *args, **kwargs):
        try:
            self.get_object().delete()
            return HttpResponseRedirect(
                reverse('adm-success', kwargs={'pk': 0}))
        except ProtectedError as exepcion:
            objecdic = {
                "mensaje": str(exepcion),
                "datos": {
                    "descripcion": ""
                }
            }
            return JsonResponse(objecdic)

    def get_success_url(self):
        return reverse('adm-success', kwargs={'pk': 0})
