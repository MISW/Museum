from django.views import generic

from backend.developments.models import Development


class HomeView(generic.TemplateView):
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            context = {
                'developments': Development.objects.order_by('title').filter(status=1, developer__is_superuser=False)
            }
        else:
            context = {
                'developments': Development.objects.order_by('title').filter(status=1, developer__is_superuser=False, is_private=False)
            }

        return self.render_to_response(context)
