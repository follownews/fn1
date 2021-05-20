from django.db import models

import uuid

class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)    
    name = models.CharField(max_length=255)
    language = models.CharField(max_length=6, null=True)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        return '%s, %s' % (self.name, self.language)


class City(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"


# class Language(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(max_length=255)

#     class Meta:
#         verbose_name = "Language"
#         verbose_name_plural = "Languages"
