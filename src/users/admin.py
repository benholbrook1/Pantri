from django.contrib import admin
from core.admin import BaseModelAdmin
from . import models

# Register your models here.
@admin.register(models.User) 
class UserAdmin(BaseModelAdmin):
    list_display = ('name', 'is_active', 'created_at')
