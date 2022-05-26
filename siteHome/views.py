from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import FormView
from django.urls import reverse_lazy

from siteHome.models import PaginaInicial


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['titulo'] = PaginaInicial.objects.order_by('-id').all()
        context['tituloTreinamento'] = PaginaInicial.objects.order_by('-id').all()
        return context
