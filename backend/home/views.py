from django.views import generic

from backend.developments.models import Development


class HomeView(generic.TemplateView):
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            context = {
                'apps': Development.objects.order_by('title').filter(status=1, user__is_staff=False)
            }
        else:
            context = {
                'apps': Development.objects.order_by('title').filter(status=1, user__is_staff=False, is_private=False)
            }

        return self.render_to_response(context)
