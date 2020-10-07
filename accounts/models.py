# https://github.com/django/django/blob/master/django/contrib/auth/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
import uuid


class CustomUser(AbstractUser):
    """Extended User Model"""

    userid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # user's generation is here
    generation = models.CharField(
        _("generation"),
        help_text=_('Specific Generation for this user.'),
        max_length=150,
        blank=True,
    )

    user_image = models.ImageField(upload_to='images/profiles', blank=True)
