from rest_framework import serializers

from apps.news import models

class NewsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.News

class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Tag