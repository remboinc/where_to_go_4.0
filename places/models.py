from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    short_description = models.TextField(verbose_name='Краткое описание', null=True, blank=True)
    long_description = HTMLField(verbose_name='Полное описание', null=True, blank=True)
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, related_name='media', on_delete=models.CASCADE, verbose_name='Место')
    image = models.ImageField(verbose_name='Фото', db_index=True)
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок фото')

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.order

    @property
    def get_absolute_image_url(self):
        return "{0}".format(self.image.url)
