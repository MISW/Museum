from django.contrib.auth.models import AbstractUser

"""Extended User Model"""
class CustomUser(AbstractUser):
    class Meta:
        verbose_name_plural = 'CustomUser'