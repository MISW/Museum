from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.utils import timezone

from django.http import request
from .forms import ProfileUpdateForm
from backend.users.models import User
from django.urls import reverse_lazy

from backend.users.models import User
from backend.models.models import DevelopmentInf

class MypageHomeView(generic.TemplateView):
    template_name = 'mypage/index.html'
    model = User

    def get(self, *args, **kwargs):
        context = {
            'apps':  DevelopmentInf.objects.filter(user__id=self.kwargs['pk'])
        }
        return self.render_to_response(context)

class ProfileUpdateView(generic.TemplateView):
    template_name = 'mypage/profile/update.html'

    def get(self, request, *args, **kwargs):
        form = ProfileUpdateForm()

        user = User.objects.get(pk=request.user.pk)
        form.fields['generation'].widget.attrs['value'] = user.generation
        form.fields['description'].initial = user.description

        context = dict(form=form)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ProfileUpdateForm(request.POST, request.FILES)
            if form.is_valid():
                user = User.objects.get(pk=request.user.pk)
                cleaned_data = form.cleaned_data
                user.generation = cleaned_data['generation']
                user.description = cleaned_data['description']
                if cleaned_data['image']:
                    user.image = cleaned_data['image']
                user.save()

                return redirect('mypage:home', request.user.pk)
        else:
            form = ProfileUpdateForm()

        return redirect('mypage:profile_update', request.user.pk)

class MypageNewView(generic.TemplateView):
    template_name = 'mypage/application/new.html'



# class MypageChangeView(generic.TemplateView):
#     template_name = 'mypage_application_change.html'
#     def get(self, request, **kwargs):
#         context = {
#             'app':  GameInf.objects.filter(id=self.kwargs['pk'])[0]
#         }
#         return self.render_to_response(context)

# class MypageProfileView(generic.TemplateView):
#     template_name = 'mypage_profile.html'
#     def get(self, request, **kwargs):

#         context = {
#             'description': GetDescription(request)
#         }
#         return self.render_to_response(context)

# class MypageGameDetailView(generic.DetailView):
#     model = GameInf
#     template_name = 'mypage_game_detail.html'

# class NewApplication(generic.TemplateView):
#     def post(self, request, *args, **kwargs):
#         g = None
#         try:
#             g = GameInf(image=request.FILES["gameImage"],user=request.user,title=request.POST["gameTitle"],description=request.POST["introduction"],status=0,submittedtime=timezone.datetime.now(),link_browser=request.POST["link_browser"],link_Windows=request.POST["link_Windows"],link_Mac=request.POST["link_Mac"],link_Android=request.POST["link_Android"],link_iOS=request.POST["link_iOS"],categoryname=request.POST["gameCategory"])
#         except Exception:
#             g = GameInf(user=request.user,title=request.POST["gameTitle"],description=request.POST["introduction"],status=0,submittedtime=timezone.datetime.now(),link_Windows=request.POST["link_Windows"],link_browser=request.POST["link_browser"],link_Mac=request.POST["link_Mac"],link_Android=request.POST["link_Android"],link_iOS=request.POST["link_iOS"],categoryname=request.POST["gameCategory"])
#         g.save()
#         return redirect('/mypage')

# class UpdateApplication(generic.TemplateView):
#     def post(self, request, *args, **kwargs):
#         g = GameInf.objects.filter(id=self.kwargs['id'])[0]
#         g.user=request.user
#         g.title=request.POST["gameTitle"]
#         g.description=request.POST["introduction"]
#         g.status=0
#         g.submittedtime=timezone.datetime.now()
#         g.link_browser=request.POST["link_browser"]
#         g.link_Windows=request.POST["link_Windows"]
#         g.link_Mac=request.POST["link_Mac"]
#         g.link_Android=request.POST["link_Android"]
#         g.link_iOS=request.POST["link_iOS"]
#         g.categoryname=request.POST["gameCategory"]
#         try:
#             g.image = request.FILES["gameImage"]
#         except Exception:
#             print("noimage")
#         g.save()
#         return redirect('/mypage')

# def DeleteApplication(request,id):
#     GameInf.objects.get(id=id).delete()
#     return redirect('/mypage')
