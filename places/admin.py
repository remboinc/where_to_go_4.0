from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin, SortableAdminBase
from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import Place, PlaceImage


class ImageInline(SortableInlineAdminMixin, admin.StackedInline):
    model = PlaceImage
    readonly_fields = ('get_preview',)
    fields = ('title', 'image', 'get_preview', 'order')

    def get_preview(self, obj):
        return format_html('<img src="{}" height="200" />', mark_safe)



@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title', 'short_description', 'lat', 'lng')
    inlines = [ImageInline]


@admin.register(PlaceImage)
class PlaceImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('image', 'order')
    ordering = ('order',)
