from django.db import models
from core.models import UUIDBaseModel

# Create your models here.
class StorageLocation(UUIDBaseModel):

    name = models.CharField(max_length=150, unique=True)
    storage_type = models.CharField(max_length=50, choices=[
        ('Frozen', 'Frozen'),
        ('Cold', 'Fridge'),
        ('Dry', 'Cupboard'),
    ], default='Dry')
    capacity = models.PercentageField(default=100)


class StoredItem(UUIDBaseModel):
    """
    Model to store items in a storage location.
    """
    item = models.ForeignKey('inventory.Item', on_delete=models.CASCADE)
    storage_location = models.ForeignKey(StorageLocation, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.item.name} in {self.storage_location.name}"