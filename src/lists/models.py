from django.db import models
from core.models import UUIDBaseModel

# Create your models here.
class List(UUIDBaseModel):
    """List model to store shopping lists.
    """
    name = models.CharField(max_length=150, unique=True)
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE, default='00000000-0000-0000-0000-000000000000' ,related_name='lists')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'lists'
        unique_together = ('name', 'created_by')

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
        unique_together = ('item', 'list')