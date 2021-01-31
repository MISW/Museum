from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('', include('backend.manage.home.urls')),
    path('developments/', include('backend.manage.developments.urls')),
]
