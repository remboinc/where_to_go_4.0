from django.contrib import admin
from .models import Place, Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description_short', 'lat', 'lng')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title','order')
