from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.views import View

from apps.servicio.models import Servicio
from ..models import Principal
from ..formstotal.login import FormLogin


class HomeTemplate(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeTemplate, self).get_context_data(**kwargs)
        context['principal'] = Principal.objects.filter(estado=True).order_by("id").last()
        servicio = Servicio.objects.all().order_by("-id")[:9]
        context['servicio'] = servicio[:3]
        context['servicio1'] = servicio[3:6]
        context['servicio2'] = servicio[6:9]
        return context


class AdministracionTemplate(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    template_name = "administracion.html"


class Login(View):
    template_name = 'login.html'
    form_class = FormLogin

    def get(self, request, *args, **kwargs):
        form = self.form_class(request)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request, request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("home-administracion"))
        return render(request, self.template_name, {'form': form})


class Logout(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse("home"))
