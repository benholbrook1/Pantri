from django.db import models
from core.models import UUIDBaseModel
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator

PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]

# Create your models here.
class StorageLocation(UUIDBaseModel):

    name = models.CharField(max_length=150, unique=True)
    storage_type = models.CharField(max_length=50, choices=[
        ('Frozen', 'Frozen'),
        ('Cold', 'Fridge'),
        ('Dry', 'Cupboard'),
    ], default='Dry')
    capacity = models.PositiveSmallIntegerField(default=0, validators=PERCENTAGE_VALIDATOR)
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE, default='00000000-0000-0000-0000-000000000000', related_name='storage_locations')

    class Meta:
        db_table = 'storage_locations'
        unique_together = ('name', 'created_by')

class StorageLocationItem(UUIDBaseModel):
    """
    Model to store items in a storage location.
    """
    item = models.ForeignKey('inventory.Item', on_delete=models.CASCADE)
    storage_location = models.ForeignKey(StorageLocation, on_delete=models.CASCADE, related_name='storage_locations')

    def __str__(self):
        return f"{self.item.name} in {self.storage_location.name}"

    class Meta:
        db_table = 'storage_location_items'
        unique_together = ('item', 'storage_location')
