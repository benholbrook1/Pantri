from django.db import models
import uuid


class UUIDBaseModel(models.Model):

    SYSTEM_USER_UUID = '00000000-0000-0000-0000-000000000000'

    def generate_uuid_str():
        return str(uuid.uuid4())
    
    @classmethod
    def get_system_user(cls):
        from . import User  # Import locally to avoid circular imports
        user, created = User.objects.get_or_create(
            uuid=cls.SYSTEM_USER_UUID,
            defaults={
                'email': 'system@example.com',
                'name': 'System User',
                'is_active': False,  # Prevent login
                'is_staff': False,
                'is_superuser': False
            }
        )
        return user

    uuid = models.CharField(
        primary_key=True,
        max_length=36,
        default=generate_uuid_str,
        editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE, null=False, blank=True, editable=False)

    class Meta:
        abstract = True
