from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.template import loader
from backapp.models import *
from django.shortcuts import redirect
from django.utils import timezone
# Create your views here.
class AdminHomeView(generic.TemplateView):
    template_name = 'admin-page.html'
    def get(self, request, **kwargs):
        context = {
            'apps':  GameInf.objects.all()
        }
        return self.render_to_response(context)

class AdminGameDetailView(generic.TemplateView):
    template_name = 'admin-game-detail.html'
    def get(self, request, **kwargs):
        context = {
            'app':  GameInf.objects.filter(id=self.kwargs['pk'])[0]
        }
        return self.render_to_response(context)

class AdminNonPublicGameDetailView(generic.TemplateView):
    template_name = 'admin-nopublic-game-detail.html'
    def get(self, request, **kwargs):
        context = {
            'app':  GameInf.objects.filter(id=self.kwargs['pk'])[0]
        }
        return self.render_to_response(context)

class AdminPublicGameDetailView(generic.TemplateView):
    template_name = 'admin-public-game-detail.html'
    def get(self, request, **kwargs):
        context = {
            'app':  GameInf.objects.filter(id=self.kwargs['pk'])[0]
        }
        return self.render_to_response(context)

class AdminNonPublicView(generic.TemplateView):
    template_name = 'admin-page-nopublic.html'
    def get(self, request, **kwargs):
        context = {
            'apps':  GameInf.objects.filter(status=2)
        }
        return self.render_to_response(context)

class AdminPublicView(generic.TemplateView):
    template_name = 'admin-page-public.html'
    def get(self, request, **kwargs):
        context = {
            'apps':  GameInf.objects.filter(status=1)
        }
        return self.render_to_response(context)

def DeleteApplication(request,id):
    GameInf.objects.get(id=id).delete()
    return redirect('/adminpage')

def PublishApplication(request,id):
    GameInf.objects.filter(id=id).update(status=1)
    return redirect('/adminpage')

def HideApplication(request,id):
    GameInf.objects.filter(id=id).update(status=2)
    return redirect('/adminpage')
