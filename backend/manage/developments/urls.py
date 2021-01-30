from django.urls import path

from . import views

app_name = 'manage_developments'
urlpatterns = [
    path('', views.DevelopmentHomeView.as_view(), name='home'),
    path('pending/', views.PendingHomeView.as_view(), name='pending_home'),
    path('public/', views.PublicHomeView.as_view(), name='public_home'),
    path('closed/', views.ClosedHomeView.as_view(), name='closed_home'),
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),
]
