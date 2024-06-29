from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', unique=True)
    short_description = models.TextField(verbose_name='Краткое описание', default='Без описания... пока', blank=True)
    long_description = HTMLField(verbose_name='Полное описание', default='Без описания... пока', blank=True)
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, related_name='images', on_delete=models.CASCADE, verbose_name='Место')
    image = models.ImageField(verbose_name='Фото', db_index=True)
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок фото', db_index=True)

    class Meta:
        ordering = ['order']
        indexes = [
            models.Index(fields=['order']),
        ]
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    @property
    def get_absolute_image_url(self):
        return f'{self.image.url}'
