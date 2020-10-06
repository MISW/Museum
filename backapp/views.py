from django.shortcuts import render
from django.views import generic

from .models import *

# Create your views here.
class IndexView(generic.TemplateView):
    #model = gameInf
    template_name = 'index.html'

"""
class DevelopersView(generic.ListView):
    #model = developPartInf
    template_name = 'developers.html'

class DeveloperDetailView(generic.DetailView):
    #model = developerInf
    template_name = 'developer-detail.html'

class GameDetalView(generic.DetailView):
    #model = gameInf
    template_name = 'game-detail.html'
"""