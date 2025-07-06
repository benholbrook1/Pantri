from rest_framework import serializers
from .models import Item
from .models import PACK_UNIT_CHOICES # import the PACK_UNIT_CHOICES from models.py so it is consistent with the model definition

class ItemSerializer(serializers.ModelSerializer):
    # uuid = serializers.UUIDField(read_only=True)
    # name = serializers.CharField(max_length=150)
    # pack_unit = serializers.ChoiceField(choices=PACK_UNIT_CHOICES, default='EA')

    class Meta:
        model = Item
        fields = ['uuid', 'name', 'pack_unit']
        read_only_fields = ['uuid']

    
