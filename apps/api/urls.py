from rest_framework import routers

from .news import views as news_views
from .media import views as media_views

router = routers.DefaultRouter()

router.register('media', media_views.MediaViewSet)
router.register('news',  news_views.NewsViewSet)
router.register('tags',  news_views.TagViewSet)

urlpatterns = router.urls
