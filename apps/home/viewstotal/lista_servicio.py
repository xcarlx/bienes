from django.views.generic import TemplateView, ListView

from ...servicio.models import Servicio
from ..formstotal import tipo_servicio


class Home(TemplateView):
    template_name = "lista_servicio/home-list.html"

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        tipo = "TE" if self.kwargs['tipo'] == 0 else "CA" if self.kwargs['tipo'] == 1 else "DE"
        context['tipo_servicio'] = tipo_servicio.TipoServicioForm(initial={"tipo_inmueble": tipo})
        return context


class ListaServicio(ListView):
    template_name = "lista_servicio/lista.html"
    model = Servicio
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListaServicio, self).get_context_data(**kwargs)
        # tipo = "TE" if self.kwargs['tipo'] == 0 else "CA" if self.kwargs['tipo'] == 1 else "DE"
        # context['servicio_list'] = Servicio.objects.filter(tipo_inmueble=tipo)
        # context['object_list'] = Servicio.objects.filter(tipo_inmueble=tipo)
        return context

    def get_queryset(self):
        tipo = "TE" if self.kwargs['tipo'] == 0 else "CA" if self.kwargs['tipo'] == 1 else "DE"
        queryset = Servicio.objects.filter(tipo_inmueble=tipo)
        return queryset
