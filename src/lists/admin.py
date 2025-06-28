from django.contrib import admin 
from . import models


# Register your models here.
class ListItemInline(admin.TabularInline):  # or use admin.StackedInline for more space
    model = models.ListItem
    extra = 0  # Don’t show extra empty rows
    # autocomplete_fields = ['item']  # Optional: If your item list is long

@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by')
    inlines = [ListItemInline] 