from django.contrib import admin
from .models import *

# Register your models here.
# name - Admin, password - 1212

admin.site.register(Player)
admin.site.register(Team)

# Админка Категорий
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',) # Поля для отображения в списке
    search_fields = ('name',) # Поля для поиска


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'is_published') # Поля для отображения в списке
    list_filter = ('category', 'is_published') # Фильтр по категории и статусу публикации
    search_fields = ('title', ' content') # Поля для поиска
    list_per_page = 10

    # Разбиение полей на секции
    fieldsets = (
        (None, {'fields': ('title', 'content', 'category')}),
        ('Дополнтиельные настройки', {'classes': ('collapse',),
                                      'fields': ('is_published', 'created_at', 'updated_at')}),
    )

    # Только для чтения полей created_at и updated_at
    readonly_fields = ('created_at', 'updated_at')
