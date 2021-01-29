from django.views import generic

from .models import Development


class DevelopmentDetailView(generic.TemplateView):
    template_name = 'developments/detail.html'
    model = Development

    def get(self, *args, **kwargs):
        context = {
            'app': Development.objects.get(pk=self.kwargs['pk'], status=1)
        }

        return self.render_to_response(context)
