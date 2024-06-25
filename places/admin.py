from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin, SortableAdminBase
from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import Place, PlaceImage

MAX_IMAGE_HEIGHT = 200
MAX_IMAGE_WIDTH = 500


class ImageInline(SortableInlineAdminMixin, admin.StackedInline):
    model = PlaceImage
    readonly_fields = ('get_preview',)
    fields = ('image', 'get_preview', 'order')

    def get_preview(self, obj):
        return format_html('<img src="{}" style="max-height: {}px; max-width: {}px;" />',
                           obj.image.url,
                           MAX_IMAGE_HEIGHT,
                           MAX_IMAGE_WIDTH,)


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title', 'short_description', 'lat', 'lng')
    inlines = [ImageInline]


@admin.register(PlaceImage)
class PlaceImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    raw_id_fields = ('place',)
    list_display = ('image', 'order')
    ordering = ('order',)
