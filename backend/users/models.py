# https://github.com/django/django/blob/master/django/contrib/auth/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
import uuid

ASSOCIATION_CHOICES = (
    (1, 'プログラミング'),
    (2, 'CG'),
    (3, 'MIDI')
)

class Association(models.Model):
    association = models.IntegerField(
        choices=ASSOCIATION_CHOICES,
        help_text=('1: programming, 2: CG, 3: MIDI')
    )

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

    association = models.ManyToManyField(
        _('association'),
        Association,
        blank=True,
        null=True
    )

    image = models.ImageField(
        _('image'),
        upload_to='images/profiles',
        blank=True,
        null=True
    )

    description = models.TextField(
        _('description'),
        help_text=('User\'s description. Editable.'),
        default=''
    )

    is_admin = models.BooleanField(
        _('is_admin'),
        help_text=('administrative authority for this user.'),
        default=False
    )

    class Meta:
        verbose_name_plural = 'User'
