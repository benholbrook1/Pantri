from django.contrib import admin
from core.admin import BaseModelAdmin
from . import models

@admin.register(models.Item) 
class ItemAdmin(BaseModelAdmin):
    list_display = ('name', 'pack_unit', 'created_at', 'created_by')

