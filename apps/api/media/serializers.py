from rest_framework import serializers

from apps.media import models

class MediaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Media
