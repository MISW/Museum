from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.template import loader
from backapp.models import *
from django.shortcuts import redirect
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
            'description': GetDescription(request)
        }
        return self.render_to_response(context)

class MypageNewView(generic.TemplateView):
    template_name = 'mypage_application_new.html'

class MypageChangeView(generic.TemplateView):
    template_name = 'mypage_application_change.html'

class MypageProfileView(generic.TemplateView):
    template_name = 'myPage_profile.html'
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
