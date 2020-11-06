from django.urls import path

from . import views

app_name = 'admin_page'
urlpatterns = [
    path('', views.AdminHomeView.as_view(), name='admin_home'),
    path('game_detail/<int:pk>/', views.AdminGameDetailView.as_view(), name='game_detail'),
    path('nonpublic_game_detail/<int:pk>/', views.AdminNonPublicGameDetailView.as_view(), name='nonpublic_game_detail'),
    path('public_game_detail/<int:pk>/', views.AdminPublicGameDetailView.as_view(), name='public_game_detail'),
    path('nonpublic/', views.AdminNonPublicView.as_view(), name='nonpublic'),
    path('public/', views.AdminPublicView.as_view(), name='public'),
    path('publish/<int:id>/', views.PublishApplication, name='publish'),
    path('hide/<int:id>/', views.HideApplication, name='hide'),
    path('delete/<int:id>/', views.DeleteApplication, name='delete'),
]
