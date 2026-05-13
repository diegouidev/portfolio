from django.contrib import admin
from django.utils.html import format_html
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('thumbnail_preview', 'title', 'category', 'technologies', 'created_at')
    list_display_links = ('thumbnail_preview', 'title')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'description', 'technologies')
    readonly_fields = ('thumbnail_preview_large',)

    def thumbnail_preview(self, obj):
        if obj.thumbnail:
            return format_html(
                '<img src="{}" style="width:60px; height:60px; '
                'object-fit:cover; border-radius:8px;" />',
                obj.thumbnail.url,
            )
        return '—'

    thumbnail_preview.short_description = 'Miniatura'

    def thumbnail_preview_large(self, obj):
        if obj.thumbnail:
            return format_html(
                '<img src="{}" style="max-width:300px; border-radius:12px;" />',
                obj.thumbnail.url,
            )
        return '—'

    thumbnail_preview_large.short_description = 'Pré-visualização'
