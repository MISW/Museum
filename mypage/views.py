from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.template import loader
from backapp.models import *
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

class MypageProfileView(generic.TemplateView):
    template_name = 'mypage_profile.html'
    def get(self, request, **kwargs):

        context = {
            'description': GetDescription(request)
        }
        return self.render_to_response(context)

class UpdateProfile(generic.TemplateView):
    def post(self, request, *args, **kwargs):
        CustomUser.objects.filter(userid=request.user.userid).update(generation=request.POST["generationInput"])
        DeveloperInf.objects.filter(user=request.user).update(description=request.POST["shortCommentInput"])
        return redirect('/mypage/profile')

class NewApplication(generic.TemplateView):
    def post(self, request, *args, **kwargs):
        g = GameInf(user=request.user,title=request.POST["gameTitle"],description=request.POST["introduction"],status=0,submittedtime=timezone.datetime.now(),link_Windows=request.POST["link_Windows"],link_Mac=request.POST["link_Mac"],link_Android=request.POST["link_Android"],link_iOS=request.POST["link_iOS"])
        g.gameid = g.id
        g.save()
        ca = None
        try:
            ca = CategoryInf.objects.get(categoryname=request.POST["gameCategory"])
        except Exception as e:
            ca = CategoryInf(categoryname=request.POST["gameCategory"])
            ca.categoryid = ca.id
            ca.save()
        c = GameCategoryInf(gameid = g.gameid,categoryid=ca.categoryid)
        c.save()
        return redirect('/mypage')

class UpdateApplication(generic.TemplateView):
    def post(self, request, *args, **kwargs):
        CustomUser.objects.filter(userid=request.user.userid).update(generation=request.POST["generationInput"])
        DeveloperInf.objects.filter(user=request.user).update(description=request.POST["shortCommentInput"])
        return redirect('/mypage')
