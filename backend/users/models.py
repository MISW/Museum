# https://github.com/django/django/blob/master/django/contrib/auth/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
import uuid


class User(AbstractUser):
    """Extended User Model"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # user's generation is here
    generation = models.IntegerField(
        _('generation'),
        help_text=('Specific Generation for this user.'),
        blank=True,
        null=True
    )

    image = models.ImageField(
        _('image'),
        upload_to='images/profiles',
        blank=True,
        null=True
    )

    isadmin = models.BooleanField(
        _('isadmin'),
        help_text=('administrative authority for this user.'),
        default=False
    )

    description = models.TextField(
        _('description'),
        help_text=('User\'s description. Editable.'),
        default=''
    )

    class Meta:
        verbose_name_plural = 'User'
