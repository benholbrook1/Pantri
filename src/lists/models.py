from django.db import models
from core.models import UUIDBaseModel

# Create your models here.
class List(UUIDBaseModel):
    """List model to store shopping lists.
    """
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'lists'

class ListItem(UUIDBaseModel):
    """Model to store items in a shopping list.
    """
    item = models.ForeignKey('inventory.Item', on_delete=models.CASCADE)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.item.name} in {self.list.name}"

    class Meta:
        db_table = 'list_items'