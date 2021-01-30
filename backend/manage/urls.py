from django.urls import path

from . import views

app_name = 'manage'
urlpatterns = [
    path('development/pending/', views.DevelopmentPendingHomeView.as_view(), name='development_pending_home'),
    path('development/public/', views.DevelopmentPublicHomeView.as_view(), name='development_public_home'),
    path('development/closed/', views.DevelopmentClosedHomeView.as_view(), name='development_closed_home'),
    # path('', views.ManageHomeView.as_view(), name='admin_home'),
    # path('game_detail/<int:pk>/', views.ManageGameDetailView.as_view(), name='game_detail'),
    # path('nonpublic_game_detail/<int:pk>/', views.ManageNonPublicGameDetailView.as_view(),
    #      name='nonpublic_game_detail'),
    # path('public_game_detail/<int:pk>/', views.ManagePublicGameDetailView.as_view(), name='public_game_detail'),
    # path('nonpublic/', views.ManageNonPublicView.as_view(), name='nonpublic'),
    # path('public/', views.ManagePublicView.as_view(), name='public'),
    # path('publish/<int:id>/', views.PublishApplication, name='publish'),
    # path('hide/<int:id>/', views.HideApplication, name='hide'),
    # path('delete/<int:id>/', views.DeleteApplication, name='delete'),
]
