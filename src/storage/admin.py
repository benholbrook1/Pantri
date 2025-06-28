from django.contrib import admin
from . import models

# Register your models here.
# Register your models here.
class StorageLocationInline(admin.TabularInline):  # or use admin.StackedInline for more space
    model = models.StorageLocationItem
    extra = 0  # Don’t show extra empty rows
    # autocomplete_fields = ['item']  # Optional: If your item list is long

@admin.register(models.StorageLocation)
class StorageLocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'storage_type', 'capacity', 'created_by', 'created_at')
    inlines = [StorageLocationInline] 