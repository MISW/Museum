from django.urls import path

from . import views

app_name = 'backapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('developers/', views.DevelopersView.as_view(), name='developers'),
]