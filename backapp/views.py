from django.http import request
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

    def get(self, request, **kwargs):

        context = {
            # urlのpkを取得して，そのpkのモデルを取得する
            'object': self.model.objects.get(pk=self.kwargs['pk']),
            'applications': GameInf.objects.all()
        }
        return self.render_to_response(context)

class GameDetalView(generic.DetailView):
    #model = GameInf
    template_name = 'game-detail.html'