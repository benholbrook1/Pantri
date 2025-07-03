from django.contrib import admin
from core.admin import BaseModelAdmin
from . import models

# Register your models here.
@admin.register(models.User) 
class UserAdmin(BaseModelAdmin):
    list_display = ('created_at', 'name', 'is_active', 'is_superuser')
    search_fields = ('name', 'is_superuser')

