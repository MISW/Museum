from django.shortcuts import render
from django.http import request
from django.views import generic

from backend.models.models import DevelopmentInf

class HomeView(generic.TemplateView):
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            context = {
                'apps': DevelopmentInf.objects.order_by('title').filter(status=1, user__is_staff=False)
            }
        else:
            context = {
                'apps': DevelopmentInf.objects.order_by('title').filter(status=1, user__is_staff=False, is_public=True)
            }

        return self.render_to_response(context)