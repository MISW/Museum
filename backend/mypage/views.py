from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.template import loader
from backend.backapp.models import *
from django.shortcuts import redirect
from django.utils import timezone
# Create your views here.

def GetDescription(request):
    str = ""
    try:
        u = DeveloperInf.objects.get(user=request.user)
        str = u.description
    except Exception as e:
        u = DeveloperInf(user=request.user,description="")
        u.save()
    return str


class MypageHomeView(generic.TemplateView):
    template_name = 'mypage_home.html'
    def get(self, request, **kwargs):

        context = {
            'description': GetDescription(request),
            'applications':  GameInf.objects.filter(user=request.user)
        }
        return self.render_to_response(context)

class MypageNewView(generic.TemplateView):
    template_name = 'mypage_application_new.html'

class MypageChangeView(generic.TemplateView):
    template_name = 'mypage_application_change.html'
    def get(self, request, **kwargs):
        context = {
            'app':  GameInf.objects.filter(id=self.kwargs['pk'])[0]
        }
        return self.render_to_response(context)

class MypageProfileView(generic.TemplateView):
    template_name = 'mypage_profile.html'
    def get(self, request, **kwargs):

        context = {
            'description': GetDescription(request)
        }
        return self.render_to_response(context)

class MypageGameDetailView(generic.DetailView):
    model = GameInf
    template_name = 'mypage_game_detail.html'



class UpdateProfile(generic.TemplateView):
    def post(self, request, *args, **kwargs):
        c = CustomUser.objects.filter(userid=request.user.userid)[0]
        c.generation = request.POST["generationInput"]
        try:
            c.user_image = request.FILES["profileImageInput"]
        except Exception:
            print("")
        c.save()
        DeveloperInf.objects.filter(user=request.user).update(description=request.POST["shortCommentInput"])
        return redirect('/mypage')

class NewApplication(generic.TemplateView):
    def post(self, request, *args, **kwargs):
        g = None
        try:
            g = GameInf(image=request.FILES["gameImage"],user=request.user,title=request.POST["gameTitle"],description=request.POST["introduction"],status=0,submittedtime=timezone.datetime.now(),link_browser=request.POST["link_browser"],link_Windows=request.POST["link_Windows"],link_Mac=request.POST["link_Mac"],link_Android=request.POST["link_Android"],link_iOS=request.POST["link_iOS"],categoryname=request.POST["gameCategory"])
        except Exception:
            g = GameInf(user=request.user,title=request.POST["gameTitle"],description=request.POST["introduction"],status=0,submittedtime=timezone.datetime.now(),link_Windows=request.POST["link_Windows"],link_browser=request.POST["link_browser"],link_Mac=request.POST["link_Mac"],link_Android=request.POST["link_Android"],link_iOS=request.POST["link_iOS"],categoryname=request.POST["gameCategory"])
        g.save()
        return redirect('/mypage')

class UpdateApplication(generic.TemplateView):
    def post(self, request, *args, **kwargs):
        g = GameInf.objects.filter(id=self.kwargs['id'])[0]
        g.user=request.user
        g.title=request.POST["gameTitle"]
        g.description=request.POST["introduction"]
        g.status=0
        g.submittedtime=timezone.datetime.now()
        g.link_browser=request.POST["link_browser"]
        g.link_Windows=request.POST["link_Windows"]
        g.link_Mac=request.POST["link_Mac"]
        g.link_Android=request.POST["link_Android"]
        g.link_iOS=request.POST["link_iOS"]
        g.categoryname=request.POST["gameCategory"]
        try:
            g.image = request.FILES["gameImage"]
        except Exception:
            print("noimage")
        g.save()
        return redirect('/mypage')

def DeleteApplication(request,id):
    GameInf.objects.get(id=id).delete()
    return redirect('/mypage')
