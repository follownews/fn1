from django.urls import path, include
# from django.contrib import admin
from django.conf.urls import url
from smarturls import surl
from django.contrib.auth import views as auth_views

from allauth.account.views import *
from apps.news import views as news_views
from apps.customuser import views as customuser_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', news_views.home, name="home"),
    path('accounts/profile/', customuser_views.profile, name="profile"),
    path('es-co/<str:slug>/', news_views.media, name='media'),
    path('medias/list/', news_views.medias, name='medias'),
    # surl('media/follow/(?P<pk>[A-Fa-f0-9]{8}-?[A-Fa-f0-9]{4}-?4[A-Fa-f0-9]{3}-?[89abAB][a-fA-F0-9]{3}-?[a-fA-F0-9]{12})/', news_views.view_follow_media, name="followmedia"),

    # path('settings/', news_views.settings, name='settings'),
    # path('settings/password/', news_views.password, name='password'),
    # path('oauth/', include('social_django.urls', namespace='social')),

    # # path('account_activation_sent/', news_views.account_activation_sent, name='account_activation_sent'),
    # path('account_activation_token/', news_views.account_activation_token, name='account_activation_token'),
    # path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', news_views.activate, name='activate'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
