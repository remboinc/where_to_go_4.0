from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField(max_length=500)
    description_long = models.TextField()
    lng = models.FloatField(default=0)
    lat = models.FloatField(default=0)

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, related_name='media', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    @property
    def get_absolute_image_url(self):
        return "{0}".format(self.image.url)

