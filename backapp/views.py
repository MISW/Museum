<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
from django.shortcuts import render
from django.views import generic

from .models import *

# Create your views here.
class IndexView(generic.TemplateView):
    #model = gameInf
    template_name = 'index.html'

class DevelopersView(generic.ListView):
    #model = developPartInf
    template_name = 'developers.html'

class DeveloperDetailView(generic.DetailView):
    #model = developerInf
    template_name = 'developer-detail.html'

class GameDetalView(generic.DetailView):
<<<<<<< HEAD
    model = gameInf
    template_name = 'game-detail.html'
>>>>>>> 11302c4c05fa880201ce46afb9e9b8369cfaa17e
=======
    #model = gameInf
    template_name = 'game-detail.html'
>>>>>>> 5f2b82838761ce19a1bc93c8f7e1370b93850a7a
