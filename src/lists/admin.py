from django.contrib import admin 
from core.admin import BaseModelAdmin
from . import models


# Register your models here.
class ListItemInline(admin.TabularInline):
    model = models.ListItem
    extra = 0  # Don’t show extra empty rows
    fields = ('created_at', 'item', 'quantity', 'created_by')
    can_delete = True
    readonly_fields = ('created_at', 'created_by', 'item')

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return True

@admin.register(models.List)
class ListAdmin(BaseModelAdmin):
    list_display = ('name', 'created_by')
    inlines = [ListItemInline] 

@admin.register(models.ListItem)
class ListItemAdmin(BaseModelAdmin):
    list_display = ('item', 'list', 'quantity', 'created_by')
