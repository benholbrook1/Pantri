from django.contrib import admin
from core.admin import BaseModelAdmin
from . import models

# Register your models here.
# Register your models here.
class StorageLocationInline(admin.TabularInline):  # or use admin.StackedInline for more space
    model = models.StorageLocationItem
    extra = 0  # Don’t show extra empty rows
    fields = ('created_at', 'item', 'quantity', 'created_by')
    can_delete = True
    readonly_fields = ('created_at', 'created_by', 'item')

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return True

@admin.register(models.StorageLocation)
class StorageLocationAdmin(BaseModelAdmin):
    list_display = ('name', 'storage_type', 'capacity', 'created_by', 'created_at')
    inlines = [StorageLocationInline] 
    search_fields = ('name', 'storage_location')

@admin.register(models.StorageLocationItem)
class StorageLocationItemAdmin(BaseModelAdmin):
    list_display = ('item', 'storage_location__name', 'quantity', 'created_by', 'created_at')
    list_filter = ('storage_location',)
    search_fields = ('item__name', 'storage_location__name')
    readonly_fields = ('created_at', 'created_by')
    autocomplete_fields = ('item', 'storage_location')
    
