from django.shortcuts import redirect
from django.utils import timezone
from django.views import generic

from backend.developments.models import Development
from backend.users.models import User
from .forms import (
    ProfileUpdateForm,
    DevelopmentCreateForm,
    DevelopmentUpdateForm,
)


class MypageHomeView(generic.TemplateView):
    template_name = 'mypage/index.html'
    model = User

    def get(self, *args, **kwargs):
        context = {
            'developments': Development.objects.filter(user__id=self.kwargs['pk'])
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

        return redirect('mypage:profile_update')


class DevelopmentNewView(generic.TemplateView):
    template_name = 'mypage/development/new.html'

    def get(self, *args, **kwargs):
        form = DevelopmentCreateForm()
        context = dict(form=form)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = DevelopmentCreateForm(request.POST, request.FILES)
            if form.is_valid():
                user = User.objects.get(pk=request.user.pk)
                cleaned_data = form.cleaned_data
                development = Development()
                development.title = cleaned_data['title']
                development.description = cleaned_data['description']
                development.user = request.user
                if cleaned_data['top_image']:
                    development.top_image = cleaned_data['top_image']
                development.is_private = cleaned_data['is_private']
                development.submitted_at = timezone.now()
                development.updated_at = timezone.now()
                development.save()

                return redirect('mypage:home', request.user.pk)
        else:
            form = DevelopmentCreateForm

        return redirect('mypage:devlopment_new')


class DevelopmentUpdateView(generic.TemplateView):
    template_name = 'mypage/development/update.html'

    def get(self, *args, **kwargs):
        form = DevelopmentUpdateForm()

        development = Development.objects.get(pk=self.kwargs['pk'])
        form.fields['title'].initial = development.title
        form.fields['description'].initial = development.description

        context = dict(form=form)
        context['development'] = development

        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        development = Development.objects.get(pk=self.kwargs['pk'])

        if request.method == 'POST':
            form = DevelopmentUpdateForm(request.POST, request.FILES)
            if form.is_valid():
                cleaned_data = form.cleaned_data
                development.title = cleaned_data['title']
                development.description = cleaned_data['description']
                development.user = request.user
                if cleaned_data['top_image']:
                    development.top_image = cleaned_data['top_image']
                development.is_private = cleaned_data['is_private']
                development.updated_at = timezone.now()
                development.save()

                return redirect('mypage:home', request.user.pk)
        else:
            form = DevelopmentUpdateForm()

        return redirect('mypage:devlopment_update', development.pk)


class DevelopmentDeleteView(generic.TemplateView):
    template_name = 'mypage/development/delete.html'

    def get(self, *args, **kwargs):
        context = {
            'development': Development.objects.get(pk=self.kwargs['pk'])
        }

        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        development = Development.objects.get(pk=self.kwargs['pk'])

        if request.method == 'POST':
            development.delete()
            return redirect('mypage:home', request.user.pk)

        return redirect('mypage:development_update', development.pk)


class DevelopmentDetailView(generic.TemplateView):
    template_name = 'mypage/development/detail.html'

    def get(self, *args, **kwargs):
        context = {
            'development': Development.objects.get(pk=self.kwargs['pk'])
        }

        return self.render_to_response(context)


# class MypageChangeView(generic.TemplateView):
#     template_name = 'mypage_application_change.html'
#     def get(self, request, **kwargs):
#         context = {
#             'development':  GameInf.objects.filter(id=self.kwargs['pk'])[0]
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
