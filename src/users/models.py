from django.db import models
from core.models import UUIDBaseModel


# Create your models here.
class User(UUIDBaseModel):
    """
    User model to store user information.
    """
    name = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username