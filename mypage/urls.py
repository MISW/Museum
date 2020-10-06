from django.urls import path

from . import views

app_name = 'mypage'
urlpatterns = [
    path('', views.MypageHomeView.as_view(), name='mypage_home'),
]