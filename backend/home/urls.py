from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('search', views.SearchView.as_view(), name='search'),
    path('getkeywords', views.keywords_api, name='keywords_api')
]
