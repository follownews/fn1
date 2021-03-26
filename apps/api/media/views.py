
from rest_framework import filters
from rest_framework import viewsets
from rest_framework import generics

from . import serializers

from apps.media import models


class MediaViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = models.Media.objects.all()
    serializer_class = serializers.MediaSerializer
