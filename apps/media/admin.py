from django.contrib import admin
from apps.media.models import Media

from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'url')
    fields = [('name', 'url'), ('country'), 'media_hi_logo', ('media_mini_logo', 'mini_logo_y_nombre'), 'visible']