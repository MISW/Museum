from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('developments/', include('backend.manage.developments.urls')),
]
