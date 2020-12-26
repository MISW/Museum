from django.urls import path

from . import views

app_name = 'backend.oauth'
urlpatterns = [
    path('logout/', views.logout)
]