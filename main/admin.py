from django.contrib import admin
from django.utils.html import format_html

from .models import (
    Banner, NewsCategory, News, Leadership, Department,
    StateSymbol, AdmissionInfo, AdmissionApplication, Olympiad, ContactMessage
)

admin.site.site_header = "SamDAQI Akademik Litseyi Boshqaruv Paneli"
admin.site.site_title = "Akademik Litsey Admin"
admin.site.index_title = "Sayt Ma'lumotlarini Boshqarish"

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'title', 'order', 'is_active', 'created_at')
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'subtitle')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 120px; height: 55px; object-fit: cover; border-radius: 6px; border: 1px solid #ddd;" />', obj.image.url)
        return "Rasm yo'q"
    image_preview.short_description = "Rasm"


@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'title', 'category', 'is_featured', 'views_count', 'created_at')
    list_filter = ('category', 'is_featured', 'created_at')
    search_fields = ('title', 'summary', 'content')
    prepopulated_fields = {'slug': ('title',)}

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 70px; height: 45px; object-fit: cover; border-radius: 4px;" />', obj.image.url)
        return "Rasm yo'q"
    image_preview.short_description = "Muqova"

@admin.register(Leadership)
class LeadershipAdmin(admin.ModelAdmin):
    list_display = ('photo_preview', 'full_name', 'position', 'phone', 'reception_hours', 'order')
    list_editable = ('order',)
    search_fields = ('full_name', 'position')

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="width: 45px; height: 45px; object-fit: cover; border-radius: 50%;" />', obj.photo.url)
        return "Foto yo'q"
    photo_preview.short_description = "Foto"


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'head_name')
    search_fields = ('name', 'code', 'head_name')

@admin.register(StateSymbol)
class StateSymbolAdmin(admin.ModelAdmin):
    list_display = ('symbol_type', 'title')

@admin.register(AdmissionInfo)
class AdmissionInfoAdmin(admin.ModelAdmin):
    list_display = ('academic_year', 'title', 'is_active')
    list_editable = ('is_active',)

@admin.register(AdmissionApplication)
class AdmissionApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'direction', 'phone', 'previous_school', 'status', 'created_at')
    list_filter = ('direction', 'status', 'created_at')
    list_editable = ('status',)
    search_fields = ('full_name', 'phone', 'previous_school', 'address')

@admin.register(Olympiad)
class OlympiadAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'event_date', 'is_active')
    list_filter = ('subject', 'is_active', 'event_date')
    search_fields = ('title', 'subject')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'phone', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
    list_editable = ('is_read',)
    search_fields = ('name', 'phone', 'subject', 'message')
