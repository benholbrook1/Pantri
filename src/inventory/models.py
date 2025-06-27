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
    remaining_quantity = models.PositiveSmallIntegerField(default=0, validators=PERCENTAGE_VALIDATOR)   
    pack_unit = models.CharField(max_length=50, default='pcs')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'item_packs'

class Item(UUIDBaseModel):
    name = models.CharField(max_length=150)
    pack = models.ForeignKey(ItemPack, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.pack.name})"

    class Meta:
        db_table = 'items'
        unique_together = ('name', 'pack')

class CatalogItem(Item):
    class Meta:
        db_table = 'catalog_items'

class UserItem(Item):
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE, default='00000000-0000-0000-0000-000000000000', related_name='user_items')

    class Meta:
        db_table = 'user_items'