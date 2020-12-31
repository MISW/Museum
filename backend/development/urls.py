from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views

app_name = 'development'
urlpatterns = [
    path('detail/<int:pk>', views.DevelopmentDetailView.as_view(), name='detail'),
]
