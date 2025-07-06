from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from core.models import UUIDBaseModel

class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        system_user = User.objects.get(uuid='00000000-0000-0000-0000-000000000000')

        extra_fields.setdefault('created_by', system_user)

        if password is None:
            raise ValueError('Superusers must have a password')
        
        return self.create_user(email, name, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin, UUIDBaseModel):
    """
    Custom user model with admin compatibility that inherits from UUIDBaseModel
    """
    name = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, blank=True, null=True)

    
    # Admin-specific fields
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'  # Use email as the login field
    REQUIRED_FIELDS = ['name']  # Required when creating superuser

    def save(self, *args, **kwargs):
        if self.uuid == '00000000-0000-0000-0000-000000000000' and not self.created_by:
            # System user can be its own creator
            self.created_by = self
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'users'