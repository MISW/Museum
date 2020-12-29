from django.urls import path

from . import views

app_name = 'backend.home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home')
]
