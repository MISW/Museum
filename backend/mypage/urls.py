from django.urls import path

from . import views

app_name = 'mypage'
urlpatterns = [
    path('<uuid:pk>/', views.MypageHomeView.as_view(), name='home'),
    path('profile/update/', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('development/new/', views.DevelopmentNewView.as_view(), name='development_new'),
    path('development/update/<int:pk>/', views.DevelopmentUpdateView.as_view(), name='development_update'),
    path('development/delete/<int:pk>/', views.DevelopmentDeleteView.as_view(), name='development_delete'),
    path('development/detail/<int:pk>/', views.DevelopmentDetailView.as_view(), name='development_detail'),
    # path('new_application/', views.NewApplication.as_view(), name='new_application'),
    # path('update_application/<int:id>', views.UpdateApplication.as_view(), name='update_application'),
    # path('delete_application/<int:id>', views.DeleteApplication, name='delete_application'),
    # path('game_detail/<int:pk>/', views.MypageGameDetailView.as_view(), name='game_detail')
]
