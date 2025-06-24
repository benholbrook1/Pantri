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
    capacity = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0), validators=PERCENTAGE_VALIDATOR)


class StoredItem(UUIDBaseModel):
    """
    Model to store items in a storage location.
    """
    item = models.ForeignKey('inventory.Item', on_delete=models.CASCADE)
    storage_location = models.ForeignKey(StorageLocation, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.item.name} in {self.storage_location.name}"