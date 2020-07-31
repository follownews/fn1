from django.urls import path, include
from django.contrib import admin
from django.conf.urls import url, include
# from smarturls import surls
from django.contrib.auth import views as auth_views

# from allauth.account.views import LoginView
from allauth.account.views import *
from apps.news import views as news_views
from apps.customuser import views as customuser_views


urlpatterns = [
    # path('', news_views.home, name="home"),
    path('', news_views.home, name="home"),
    path('accounts/profile/', customuser_views.profile, name="profile")
    # path('accounts/profile/', news_views.profile, name="profile"),

    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),     # OK, pero con el logout de admin
    # path('signup/', news_views.signup, name='signup'),

    # path('settings/', news_views.settings, name='settings'),
    # path('settings/password/', news_views.password, name='password'),
    # path('oauth/', include('social_django.urls', namespace='social')),

    # # path('account_activation_sent/', news_views.account_activation_sent, name='account_activation_sent'),
    # path('account_activation_token/', news_views.account_activation_token, name='account_activation_token'),
    # path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', news_views.activate, name='activate'),
]
