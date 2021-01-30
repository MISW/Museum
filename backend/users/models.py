# https://github.com/django/django/blob/master/django/contrib/auth/models.py

import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_comma_separated_integer_list


ASSOCIATION_CHOICES = (
    (0, 'プログラミング'),
    (1, 'CG'),
    (2, 'MIDI')
)

class User(AbstractUser):
    """Extended User Model"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # user's generation is here
    generation = models.IntegerField(
        _('generation'),
        help_text='Specific Generation for this user.',
        blank=True,
        null=True
    )

    associations = models.CharField(
        _('associations'),
        validators=[validate_comma_separated_integer_list],
        max_length=6,
        help_text='0: programming, 1: CG, 2: MIDI',
        blank=True,
        null=True,
        default=''
    )

    image = models.ImageField(
        _('image'),
        upload_to='images/User',
        blank=True,
        null=True
    )

    description = models.TextField(
        _('description'),
        help_text='User\'s description. Editable.',
        blank=True,
        null=True,
        default=''
    )

    is_admin = models.BooleanField(
        _('is_admin'),
        help_text='administrative authority for this user.',
        default=False
    )

    class Meta:
        verbose_name_plural = 'User'

    def get_associations(self) -> list:
        associations = self.associations
        associations_int_list = associations.split(',')
        associations_str_list = []
        for association in associations_int_list:
            for choice in ASSOCIATION_CHOICES:
                num = choice[0]
                name = choice[1]
                if association == num:
                    association.append(name)

        return associations_str_list
