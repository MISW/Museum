from django.shortcuts import render
from django.views import generic

from .models import *

# Create your views here.
class MypageHomeView(generic.TemplateView):
    template_name = 'mypage_home.html'
