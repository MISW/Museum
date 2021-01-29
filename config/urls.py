"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from .settings_common import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('social_django.urls')),
    path('', include('backend.oauth.urls')),
    path('', include('backend.home.urls')),
    path('developers/', include('backend.developers.urls')),
    path('', include('backend.developments.urls')),
    path('', include('backend.contact.urls')),
    path('mypage/', include('backend.mypage.urls')),
    # path('manage/', include('backend.manage.urls')),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
