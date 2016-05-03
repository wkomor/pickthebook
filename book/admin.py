from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Item


class ItemAdmin(MPTTModelAdmin):
    list_display = ('title', 'text')


admin.site.register(Item, ItemAdmin)