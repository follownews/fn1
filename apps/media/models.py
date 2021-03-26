from django.db import models
from django.urls import reverse, reverse_lazy
from autoslug import AutoSlugField

import uuid


def user_directory_path(instance, filename):
    return '{}/{}'.format(instance.slug, filename)


class Media(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    url = models.URLField()
    languages = models.ManyToManyField("country.Language", blank=True)
    country = models.ForeignKey("country.Country", related_name='medias', on_delete=models.CASCADE)
    # city = models.ForeignKey("country.City", null=True, blank=True, related_name='medias')
    slug = AutoSlugField(populate_from='name', unique=True)
    visible = models.BooleanField('¿Tiene vista previa?', default=True)
    media_mini_logo = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    mini_logo_y_nombre = models.BooleanField('Mostrar ninilogo y nombre', default=True)
    media_hi_logo = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    read = models.BooleanField('Noticia leída', default=False)

    class Meta:
        verbose_name = "Media"
        verbose_name_plural = "Medias"

    def __str__(self):
        return self.name

    def get_news_url(self):
        return reverse_lazy("news", kwargs={"slug": self.slug})

    # def get_absolute_url(self):
    #     """Intenté, pero no funcionó
    #     """
    #     return reverse('media-detail', args=[self.id]) # kwargs={'uuid': self.id}) # args=[self.id]) # kwargs={'slug': self.slug})


class DefaultMedia(models.Model):
    """
    Esta tabla parece que no tiene función definida
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
