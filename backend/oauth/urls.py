from django.urls import path

from . import views

app_name = 'oauth'
urlpatterns = [
    path('logout/', views.logout)
]
