# ga-django-python/core/views.py

from urllib.parse import urlencode

from django.conf import settings
from django.contrib.auth import logout as log_out
from django.http import HttpResponseRedirect


# Create your views here.
def logout(request):
    log_out(request)
    return_to = urlencode({"returnTo": request.build_absolute_uri("/")})
    logout_url = "https://{}/v2/logout?client_id={}&{}".format(
        settings.SOCIAL_AUTH_AUTH0_DOMAIN, settings.SOCIAL_AUTH_AUTH0_KEY, return_to,
    )
    return HttpResponseRedirect(logout_url)
