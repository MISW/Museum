from django.urls import path

from . import views

app_name = 'mypage'
urlpatterns = [
    path('', views.MypageHomeView.as_view(), name='mypage_home'),
    path('new', views.MypageNewView.as_view(), name='new'),
    path('change', views.MypageChangeView.as_view(), name='change'),
    path('profile', views.MypageProfileView.as_view(), name='profile'),
    path('update_profile', views.UpdateProfile.as_view(), name='update_profile'),
    path('new_application', views.NewApplication.as_view(), name='new_application')
]
