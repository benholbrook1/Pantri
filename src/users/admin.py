from django.contrib import admin
from core.admin import BaseModelAdmin
from . import models

# Register your models here.
@admin.register(models.User) 
class UserAdmin(BaseModelAdmin):
    list_display = ('uuid','created_at', 'name', 'is_active', 'is_superuser')
    readonly_fields = ('uuid', 'created_at', 'last_login', 'created_by')
    search_fields = ('name', 'is_superuser')
    exclude = ('password', 'groups', 'user_permissions')  # Exclude password field for security reasons

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