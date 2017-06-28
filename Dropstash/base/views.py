from django.shortcuts import render
from django.views.generic.base import TemplateView


class PageView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        return context


class LandingView(PageView):
    template_name = 'base/home.html'
