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
                if cleaned_data['media_type'] and cleaned_data['file']:
                    media_flag = True
                    media = Media()
                    media.type = cleaned_data['media_type']
                    media.file = cleaned_data['file']
                    media.save()

            link_flag = False
            if link_form.is_valid():
                cleaned_data = link_form.cleaned_data
                if cleaned_data['link_type'] and cleaned_data['link']:
                    link_flag = True
                    link = Link()
                    link.type = cleaned_data['link_type']
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
        development = Development.objects.get(pk=self.kwargs['pk'])
        media = development.medias.first()
        media_flag = bool(media)
        link = development.links.first()
        link_flag = bool(link)
        development_form_initial = {
            'title': development.title,
            'description': development.description,
            'associations': development.get_associations(),
            'is_private': development.is_private,
            'top_image': [ development.top_image if development.top_image else None]
        }
        if media_flag:
            media_form_initial = {
                'media_type': media.type,
                'file': media.file
            }
        else:
            media_form_initial = {}

        if link_flag:
            link_form_initial = {
                'link_type': link.type,
                'link': link.link
            }
        else:
            link_form_initial = {}

        development_form = DevelopmentCreateForm(initial=development_form_initial)
        media_form = MediaCreateForm(initial=media_form_initial)
        link_form = LinkCreateForm(initial=link_form_initial)
        development_form.fields['co_developers'].queryset = (
            User.objects.filter(is_superuser=False)
                .exclude(pk=self.request.user.pk)
        )
        development_form.fields['co_developers'].initial = (
            [co_developer.pk for co_developer in development.co_developers.all()]
        )

        context = {
            'development': development,
            'development_form': development_form,
            'media_form': media_form,
            'link_form': link_form
        }

        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        development = Development.objects.get(pk=self.kwargs['pk'])
        media_exists = False
        if development.medias.exists():
            media_exists = True
            media = development.medias.first()
        link_exists = False
        if development.links.exists():
            link = development.links.first()

        if request.method == 'POST':
            development_form = DevelopmentCreateForm(request.POST, request.FILES)
            media_form = MediaCreateForm(request.POST, request.FILES)
            link_form = LinkCreateForm(request.POST)

            media_flag = False
            if media_form.is_valid():
                cleaned_data = media_form.cleaned_data
                if str(cleaned_data['file']) == 'False':
                    media.delete()
                elif cleaned_data['media_type'] and cleaned_data['file']:
                    if not media_exists:
                        media = Media()
                    media_flag = True
                    media.type = cleaned_data['media_type']
                    media.file = cleaned_data['file']
                    media.save()

            link_flag = False
            if link_form.is_valid():
                cleaned_data = link_form.cleaned_data
                if cleaned_data['link_type'] and cleaned_data['link']:
                    if not link_exists:
                        link = Link()
                    link_flag = True
                    link.type = cleaned_data['link_type']
                    link.link = cleaned_data['link']
                    link.save()

            if development_form.is_valid():
                cleaned_data = development_form.cleaned_data
                development.title = cleaned_data['title']
                development.description = cleaned_data['description']
                if str(cleaned_data['top_image']) == 'False':
                    development.top_image.delete()
                elif cleaned_data['top_image']:
                    development.top_image = cleaned_data['top_image']
                development.associations = ','.join(cleaned_data['associations'])
                development.is_private = cleaned_data['is_private']
                development.save()

                development.co_developers.clear()
                for co_developer in development_form.cleaned_data['co_developers']:
                    development.co_developers.add(co_developer)

                if media_flag:
                    development.medias.add(media)
                if link_flag:
                    development.links.add(link)

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
