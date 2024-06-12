from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin, SortableAdminBase
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Place, PlaceImage


class ImageInline(SortableInlineAdminMixin, admin.StackedInline):
    model = PlaceImage
    readonly_fields = ('get_preview',)
    fields = ('title', 'image', 'get_preview', 'order')

    def get_preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" height="200" />')


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title', 'description_short', 'lat', 'lng')
    inlines = [ImageInline]


@admin.register(PlaceImage)
class PlaceImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'order')
    ordering = ('order',)
