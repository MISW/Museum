from django.http import request
from django.shortcuts import render
from django.views import generic
from .models import *
from django.db.models import Q

# Create your views here.
class IndexView(generic.ListView):
    model = GameInf
    template_name = 'index.html'

class SearchView(generic.TemplateView):
    template_name = 'index.html'
    def post(self, request, *args, **kwargs):
        keyword = request.POST['search']
        list = GameInf.objects.all()
        if keyword:
            list = GameInf.objects.filter(title__icontains=keyword)
        category = request.POST.get('category')
        if category:
            list = list.filter(categoryname=category)
        kisyu = request.POST.getlist('kisyu[]')
        print("/////////////////////////////")
        print(kisyu)
        print("/////////////////////////////")
        my_filter_qs = Q()
        for k in kisyu:
            if k == "Windows":
                my_filter_qs = my_filter_qs | ~Q(link_Windows="")
            elif k =="Mac":
                my_filter_qs = my_filter_qs | ~Q(link_Mac="")
            elif k =="Android":
                my_filter_qs = my_filter_qs | ~Q(link_Android="")
            elif k =="iOS":
                my_filter_qs = my_filter_qs | ~Q(link_iOS="")
            elif k =="Browser":
                my_filter_qs = my_filter_qs | ~Q(link_browser="")
        list = list.filter(my_filter_qs)
        context = {
            # urlのpkを取得して，そのpkのモデルを取得する
            'object_list': list,
            'keyword':keyword
        }
        return self.render_to_response(context)

class AboutView(generic.TemplateView):
    template_name = 'about.html'

class DevelopersView(generic.ListView):
    model = DeveloperInf
    template_name = 'developers.html'

class DeveloperDetailView(generic.DetailView):
    model = DeveloperInf
    template_name = 'developer-detail.html'

    def get(self, request, **kwargs):

        context = {
            # urlのpkを取得して，そのpkのモデルを取得する
            'object': self.model.objects.get(pk=self.kwargs['pk']),
            'applications': GameInf.objects.all()
        }
        return self.render_to_response(context)

class GameDetalView(generic.DetailView):
    model = GameInf
    template_name = 'game-detail.html'
