from django.urls import path

from . import views

app_name = 'backapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('developers/', views.DevelopersView.as_view(), name='developers'),
    path('developer-detail/<int:pk>/', views.DeveloperDetailView.as_view(), name='developer-detail'),
    path('game-detail/<int:pk>/', views.GameDetalView.as_view(), name='game-detail'),
]