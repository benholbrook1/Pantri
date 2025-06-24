from django.db import models
from core.models import UUIDBaseModel
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator


PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]
# Create your models here.

class ItemPack(UUIDBaseModel):
    """
    ItemPack model to store item pack information.
    """
    name = models.CharField(max_length=150, unique=True)
    total_quantity = models.PositiveIntegerField(default=0)
    remaining_quantity = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0), validators=PERCENTAGE_VALIDATOR)
    pack_unit = models.CharField(max_length=50, default='pcs')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'item_pack'

class Item(UUIDBaseModel):
    """
    Item model to store item information.
    """
    name = models.CharField(max_length=150, unique=True)
    pack_uuid = models.ForeignKey(ItemPack, on_delete=models.CASCADE)

    def __str__(self):
        return self.name