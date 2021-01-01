from django.urls import path

from . import views

app_name = 'mypage'
urlpatterns = [
    path('<uuid:pk>/', views.MypageHomeView.as_view(), name='home'),
    path('profile/update/', views.ProfileUpdateView.as_view(), name='profile_update'),
    # path('new/', views.MypageNewView.as_view(), name='new'),
    # path('change/<int:pk>/', views.MypageChangeView.as_view(), name='change'),
    # path('update_profile/', views.UpdateProfile.as_view(), name='update_profile'),
    # path('new_application/', views.NewApplication.as_view(), name='new_application'),
    # path('update_application/<int:id>', views.UpdateApplication.as_view(), name='update_application'),
    # path('delete_application/<int:id>', views.DeleteApplication, name='delete_application'),
    # path('game_detail/<int:pk>/', views.MypageGameDetailView.as_view(), name='game_detail')
]
