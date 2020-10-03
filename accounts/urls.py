from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('mypage_home/', views.MypageHomeView.as_view(), name='mypage_home'),
]