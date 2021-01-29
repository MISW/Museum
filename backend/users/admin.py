from django.contrib import admin

from .models import User, Association

# Register your models here.
admin.site.register(User)
admin.site.register(Association)
