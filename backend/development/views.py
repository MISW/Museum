from django.db import models
from django.shortcuts import render
from django.http import request
from django.views import generic

from backend.models.models import DevelopmentInf


class DevelopmentDetailView(generic.TemplateView):
    template_name = 'development/detail.html'
    model = DevelopmentInf

    def get(self, *args, **kwargs):
        context = {
            'app': DevelopmentInf.objects.get(pk=self.kwargs['pk'], status=1)
        }

        return self.render_to_response(context)