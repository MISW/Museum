from django.views import generic

from backend.models.models import DevelopmentInf
from backend.users.models import User


class DevelopersView(generic.TemplateView):
    template_name = 'developers/index.html'

    def get(self, *args, **kwargs):
        context = {
            'developers': User.objects.order_by('generation', 'username').filter(is_staff=False)
        }

        return self.render_to_response(context)


class DevelopersDetailView(generic.TemplateView):
    template_name = 'developers/detail.html'
    model = User

    def get(self, *args, **kwargs):
        context = {
            'developer': self.model.objects.get(pk=self.kwargs['pk']),
            'apps': DevelopmentInf.objects.filter(user__id=self.kwargs['pk'], status=1)
        }

        return self.render_to_response(context)
