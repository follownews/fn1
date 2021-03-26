
from rest_framework import filters
from rest_framework import viewsets
from rest_framework import generics

from . import serializers

from apps.news import models


class NewsViewSet(viewsets.ModelViewSet):

    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer


class TagViewSet(viewsets.ModelViewSet):

    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer