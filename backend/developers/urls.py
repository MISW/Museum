from django.urls import path

from . import views

app_name = 'backend.developers'
urlpatterns = [
    path('', views.DevelopersView.as_view(), name='home'),
    path('detail/<uuid:pk>', views.DeveloperDetailView.as_view(), name='detail'),
]
