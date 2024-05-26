from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField(max_length=500)
    description_long = models.TextField()
    lng = models.FloatField(default=0)
    lat = models.FloatField(default=0)

    def __str__(self):
        return self.title
