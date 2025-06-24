from django.db import models
from core.models import UUIDBaseModel


# Create your models here.
class Item(UUIDBaseModel):
    """
    Item model to store item information.
    """
    name = models.CharField(max_length=150, unique=True)
    pack_uuid = models.UUIDField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

class ItemPack(UUIDBaseModel):
    """
    ItemPack model to store item pack information.
    """
    name = models.CharField(max_length=150, unique=True)
    total_quantity = models.PositiveIntegerField(default=0)
    remaining_quantity = models.PercentageField(default=100)
    pack_unit = models.CharField(max_length=50, default='pcs')

    def __str__(self):
        return self.name