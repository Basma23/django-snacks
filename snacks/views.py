from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'snacks-home.html' # add a template

class AboutView(TemplateView):
    template_name = 'snacks-about.html'