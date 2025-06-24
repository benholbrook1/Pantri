from django.db import models
from core.models import UUIDBaseModel

# Create your models here.
class List(UUIDBaseModel):
    """List model to store shopping lists.
    """
    name = models.CharField(max_length=150, unique=True)
    items = models.ManyToManyField('inventory.Item', through='ListItem')

    def __str__(self):
        return self.name