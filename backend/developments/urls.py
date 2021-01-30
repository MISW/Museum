from django.urls import path

from . import views

app_name = 'developments'
urlpatterns = [
    path('detail/<int:pk>/', views.DevelopmentDetailView.as_view(), name='detail'),
]
