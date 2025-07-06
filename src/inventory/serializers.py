from rest_framework import serializers
from .models import Item
from .models import PACK_UNIT_CHOICES # import the PACK_UNIT_CHOICES from models.py so it is consistent with the model definition

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ['uuid', 'name', 'pack_unit', 'is_active']
        read_only_fields = ['uuid']

    
