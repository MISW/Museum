from django.urls import path

from . import views

app_name = 'mypage'
urlpatterns = [
    path('<uuid:pk>/', views.MypageHomeView.as_view(), name='home'),
    path('profile/update/', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('developments/new/', views.DevelopmentNewView.as_view(), name='developments_new'),
    path('developments/update/<int:pk>/', views.DevelopmentUpdateView.as_view(), name='developments_update'),
    path('developments/delete/<int:pk>/', views.DevelopmentDeleteView.as_view(), name='developments_delete'),
    path('developments/detail/<int:pk>/', views.DevelopmentDetailView.as_view(), name='developments_detail'),
    # path('new_application/', views.NewApplication.as_view(), name='new_application'),
    # path('update_application/<int:id>', views.UpdateApplication.as_view(), name='update_application'),
    # path('delete_application/<int:id>', views.DeleteApplication, name='delete_application'),
    # path('game_detail/<int:pk>/', views.MypageGameDetailView.as_view(), name='game_detail')
]
