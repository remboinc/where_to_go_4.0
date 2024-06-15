from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    short_description = models.TextField(verbose_name='Краткое описание')
    long_description = HTMLField(verbose_name='Полное описание')
    lng = models.FloatField(default=0, verbose_name='Долгота')
    lat = models.FloatField(default=0, verbose_name='Широта')

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, related_name='media', on_delete=models.CASCADE, verbose_name='Место')
    title = models.CharField(max_length=200, verbose_name='Название места')
    image = models.ImageField(verbose_name='Фото')
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок фото')

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    @property
    def get_absolute_image_url(self):
        return "{0}".format(self.image.url)
