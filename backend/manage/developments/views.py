from django.shortcuts import redirect
from django.views import generic

from backend.developments.models import Development
from .forms import StatusUpdateForm


class DevelopmentHomeView(generic.TemplateView):
    template_name = 'manage/developments/index.html'

    def get(self, *args, **kwargs):
        context = {
            'developments': Development.objects.all().order_by('updated_at')
        }

        return self.render_to_response(context)


class PendingHomeView(generic.TemplateView):
    template_name = 'manage/developments/pending/index.html'

    def get(self, *args, **kwargs):
        context = {
            'developments': Development.objects.filter(status=0).order_by('updated_at')
        }

        return self.render_to_response(context)


class PublicHomeView(generic.TemplateView):
    template_name = 'manage/developments/public/index.html'

    def get(self, *args, **kwargs):
        context = {
            'developments': Development.objects.filter(status=1).order_by('updated_at')
        }

        return self.render_to_response(context)


class ClosedHomeView(generic.TemplateView):
    template_name = 'manage/developments/closed/index.html'

    def get(self, *args, **kwargs):
        context = {
            'developments': Development.objects.filter(status=2).order_by('updated_at')
        }

        return self.render_to_response(context)


class DetailView(generic.TemplateView):
    template_name = 'manage/developments/detail.html'

    def get(self, *args, **kwargs):
        development = Development.objects.get(pk=self.kwargs['pk'])

        form = StatusUpdateForm(initial={
            'status': development.status
        })

        context = dict(form=form)

        context['development'] = development

        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        development = Development.objects.get(pk=self.kwargs['pk'])
        previous_status = development.status
        print(type(previous_status))

        if request.method == 'POST':
            form = StatusUpdateForm(request.POST)
            if form.is_valid():
                cleaned_data = form.cleaned_data
                development.status = cleaned_data['status']
                development.save()

                if previous_status == 0:
                    return redirect('manage_developments:pending_home')
                elif previous_status == 1:
                    return redirect('manage_developments:public_home')
                elif previous_status == 2:
                    return redirect('manage_developments:closed_home')
        else:
            form = StatusUpdateForm()

        return redirect('manage_developments:detail', development.pk)
