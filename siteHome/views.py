from django.shortcuts import render

from django.views.generic import TemplateView
from django.views.generic import FormView
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = "index.html"

    def get_content_data(self, kwargs):
        context = super(IndexView, self).get_content_data(kwargs)
        return context
