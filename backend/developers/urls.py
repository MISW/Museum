from django.urls import path

from . import views

app_name = 'developers'
urlpatterns = [
    path('', views.DevelopersView.as_view(), name='home'),
    path('detail/<uuid:pk>/', views.DevelopersDetailView.as_view(), name='detail'),
]
