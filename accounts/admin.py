# https://github.com/django/django/blob/master/django/contrib/auth/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import gettext, gettext_lazy as _

from .models import CustomUser, Generation

# Register your models here.
@admin.register(Generation)
class AdminGeneration(admin.ModelAdmin):
    pass

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('full_name', 'email', 'generation')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'full_name', 'is_staff')
    search_fields = ('username', 'full_name', 'email')
    filter_horizontal = ('groups', 'user_permissions', 'generation')

admin.site.register(CustomUser, CustomUserAdmin)