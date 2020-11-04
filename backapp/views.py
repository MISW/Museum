from django.shortcuts import render
from django.views import generic

from .models import *

# Create your views here.
class IndexView(generic.ListView):
    model = GameInf
    template_name = 'index.html'

class DevelopersView(generic.ListView):
    model = DeveloperInf
    template_name = 'developers.html'

class DeveloperDetailView(generic.DetailView):
    model = DeveloperInf
    template_name = 'developer-detail.html'

class GameDetalView(generic.DetailView):
    #model = GameInf
    template_name = 'game-detail.html'