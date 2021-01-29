from django.views import generic

from backend.developments.models import Development
from backend.users.models import User


class DevelopersView(generic.TemplateView):
    template_name = 'developers/index.html'

    def get(self, *args, **kwargs):
        context = {
            'developers': User.objects.filter(is_staff=False).order_by('generation', 'username')
        }

        return self.render_to_response(context)


class DevelopersDetailView(generic.TemplateView):
    template_name = 'developers/detail.html'
    model = User

    def get(self, *args, **kwargs):
        context = {
            'developer': self.model.objects.get(pk=self.kwargs['pk']),
            'apps': Development.objects.filter(user__id=self.kwargs['pk'], status=1).order_by('updated_at')
        }

        return self.render_to_response(context)
