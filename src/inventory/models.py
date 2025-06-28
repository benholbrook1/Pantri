from django.db import models
from core.models import UUIDBaseModel
from django.core.validators import MinValueValidator, MaxValueValidator


PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]
PACK_UNIT_CHOICES = [
    ('BX', 'BOX'),
    ('PCS', 'PIECES'),
    ('BG', 'BAG'),
    ('CONT', 'CONTAINER'),
    ('JR', 'JAR'),
    ('EA', 'EACH'),
    ('PK', 'PACK'),
    ('JG', 'JUG'),
    ('BT', 'BOTTLE'),
    ('CAN', 'CAN'),
    ('TUB', 'TUB'),
    ('CT', 'CARTON'),
    ('SAC', 'SACK'),
]

class Item(UUIDBaseModel):
    name = models.CharField(max_length=150)
    total_quantity = models.PositiveIntegerField(default=0)
    remaining_percentage = models.PositiveSmallIntegerField(default=0, validators=PERCENTAGE_VALIDATOR)  
    pack_unit = models.CharField(max_length=5, choices=PACK_UNIT_CHOICES, default='EA')
    price_in_micros = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.name} ({self.pack_unit})"

    class Meta:
        db_table = 'items'
        unique_together = ('name', 'pack_unit')
