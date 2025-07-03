from django.contrib import admin
from core.admin import BaseModelAdmin
from . import models

@admin.register(models.Item) 
class ItemAdmin(BaseModelAdmin):
    list_display = ('name', 'pack_unit', 'created_at', 'created_by')
    search_fields = ('name', 'created_by__name')
    readonly_fields = ('uuid','created_at', 'created_by', 'price_in_micros')
    fields = (
        'uuid',
        'name',
        'pack_unit',
        'created_by',
        'created_at',
    )

