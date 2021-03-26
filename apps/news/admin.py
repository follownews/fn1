from django.contrib import admin
from apps.news.models import FollowNew, News, ReadLater, MediaInterest

admin.site.register(News)
admin.site.register(ReadLater)
admin.site.register(FollowNew)
admin.site.register(MediaInterest)