from django.contrib import admin
from core.admin import BaseModelAdmin
from . import models

# Register your models here.
@admin.register(models.User) 
class UserAdmin(BaseModelAdmin):
    list_display = ('name', 'created_at', 'is_active', 'is_superuser')
    readonly_fields = ('uuid', 'created_at', 'last_login', 'created_by')
    search_fields = ('name',)
    exclude = ('password', 'groups', 'user_permissions') 

    fields = (
        'uuid',
        'created_at',
        'name',
        'email',
        'is_active',
        'is_staff',
        'is_superuser',
        'last_login',
        'created_by',
    )