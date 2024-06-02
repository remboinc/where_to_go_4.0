from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin, SortableAdminBase
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.StackedInline):
    model = Image
    readonly_fields = ('get_preview',)
    fields = ('title', 'image', 'get_preview', 'order')

    def get_preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" height="200" />')


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title', 'description_short', 'lat', 'lng')
    inlines = [ImageInline]


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'order')
    ordering = ('order',)
