from backend.backapp.views import AboutView
from django.urls import path

from . import views

app_name = 'backend.backapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('developers/', views.DevelopersView.as_view(), name='developers'),
    path('developer-detail/<int:pk>/', views.DeveloperDetailView.as_view(), name='developer-detail'),
    path('game-detail/<int:pk>/', views.GameDetalView.as_view(), name='game-detail'),
]
