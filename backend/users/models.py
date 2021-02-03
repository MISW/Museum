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

ROLE_CHOICES = (
    (0, 'admin'),
    (1, 'member')
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
        upload_to='users/images',
        blank=True,
        null=True
    )

    description = models.TextField(
        _('description'),
        help_text='User\'s description. Editable.',
        blank=True,
        null=False,
        default=''
    )

    role = models.IntegerField(
        _('role'),
        choices=ROLE_CHOICES,
        help_text='0: admin, 1: member',
        default=1
    )

    class Meta:
        verbose_name_plural = 'User'


    def get_associations(self) -> list:
        associations = self.associations
        if not associations:
            return []
        return associations.split(',')

    def get_associations_display(self) -> str:
        return ', '.join(
            [ASSOCIATION_CHOICES[int(data)][1] for data in self.get_associations()]
        )


