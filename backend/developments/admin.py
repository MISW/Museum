from django.contrib import admin

from .models import Media, Link, Development

# Register your models here.
admin.site.register(Development)
admin.site.register(Media)
admin.site.register(Link)
