from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Item, Book, Genre


class ItemAdmin(MPTTModelAdmin):
    list_display = ('text',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_fields = ('description', 'author', 'item')


@admin.register(Genre)
class Genre(admin.ModelAdmin):
    fields = ['name']

admin.site.register(Item, ItemAdmin)
