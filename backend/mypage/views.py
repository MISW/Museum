from django.shortcuts import redirect
from django.utils import timezone
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from backend.developments.models import (
    Development,
    Media,
    Link
)
from backend.users.models import User
from .forms import (
    ProfileUpdateForm,
    DevelopmentCreateForm,
    DevelopmentUpdateForm,
    MediaCreateForm,
    LinkCreateForm
)


class MypageHomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'mypage/index.html'
    model = User

    def get(self, *args, **kwargs):
        context = {
            'developments': Development.objects.filter(developer_id=self.kwargs['pk'])
        }
        return self.render_to_response(context)


class ProfileUpdateView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'mypage/profile/update.html'

    def get(self, request, *args, **kwargs):
        form = ProfileUpdateForm(
            initial={
                'associations': request.user.get_associations()
            }
        )

        user = self.request.user
        form.fields['generation'].widget.attrs['value'] = user.generation
        form.fields['description'].initial = user.description

        context = dict(form=form)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ProfileUpdateForm(request.POST, request.FILES)
            if form.is_valid():
                user = self.request.user
                cleaned_data = form.cleaned_data
                user.generation = cleaned_data['generation']
                user.associations = ','.join(cleaned_data['associations'])
                user.description = cleaned_data['description']
                if cleaned_data['image']:
                    user.image = cleaned_data['image']
                user.save()

                return redirect('mypage:home', request.user.pk)
        else:
            form = ProfileUpdateForm()

        return redirect('mypage:profile_update')


class DevelopmentNewView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'mypage/developments/new.html'

    def get(self, *args, **kwargs):
        development_form = DevelopmentCreateForm()
        media_form = MediaCreateForm()
        link_form = LinkCreateForm()
        development_form.fields['co_developers'].queryset = (
            User.objects.filter(is_superuser=False)
                .exclude(pk=self.request.user.pk)
        )

        context = {
            'development_form': development_form,
            'media_form': media_form,
            'link_form': link_form
        }
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            development_form = DevelopmentCreateForm(request.POST, request.FILES)
            media_form = MediaCreateForm(request.POST, request.FILES)
            link_form = LinkCreateForm(request.POST)

            media_flag = False
            if media_form.is_valid():
                cleaned_data = media_form.cleaned_data
                if cleaned_data['type'] and cleaned_data['file']:
                    media_flag = True
                    media = Media()
                    media.type = cleaned_data['type']
                    media.file = cleaned_data['file']
                    media.save()

            link_flag = False
            if link_form.is_valid():
                cleaned_data = link_form.cleaned_data
                if cleaned_data['type'] and cleaned_data['link']:
                    link_flag = True
                    link = Link()
                    link.type = cleaned_data['type']
                    link.link = cleaned_data['link']
                    link.save()

            if development_form.is_valid():
                cleaned_data = development_form.cleaned_data
                development = Development()
                development.title = cleaned_data['title']
                development.description = cleaned_data['description']
                development.developer = request.user
                if cleaned_data['top_image']:
                    development.top_image = cleaned_data['top_image']
                development.associations = ','.join(cleaned_data['associations'])
                development.is_private = cleaned_data['is_private']
                development.save()

                for co_developer in development_form.cleaned_data['co_developers']:
                    development.co_developers.add(co_developer)

                if media_flag:
                    development.medias.add(media)
                if link_flag:
                    development.links.add(link)

                development.submitted_at = timezone.now()
                development.updated_at = timezone.now()
                development.save()

                return redirect('mypage:home', request.user.pk)
        else:
            form = DevelopmentCreateForm

        return redirect('mypage:devlopments_new')


class DevelopmentUpdateView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'mypage/developments/update.html'

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

        return redirect('mypage:devlopments_update', development.pk)


class DevelopmentDeleteView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'mypage/developments/delete.html'

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

        return redirect('mypage:developments_update', development.pk)


class DevelopmentDetailView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'mypage/developments/detail.html'

    def get(self, *args, **kwargs):
        context = {
            'development': Development.objects.get(pk=self.kwargs['pk'])
        }

        return self.render_to_response(context)
