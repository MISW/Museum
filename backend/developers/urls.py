from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views

app_name = 'developers'
urlpatterns = [
    path('', views.DevelopersView.as_view(), name='home'),
    path('detail/<uuid:pk>', views.DeveloperDetailView.as_view(), name='detail'),
]
