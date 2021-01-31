from django.urls import path

from . import views

app_name = 'manage_home'
urlpatterns = [
    path('', views.ManageHomeView.as_view(), name='home'),
]
