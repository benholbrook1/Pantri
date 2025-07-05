from rest_framework import serializers
from .models import List, ListItem
from inventory.serializers import ItemSerializer
    
class ListSerializer(serializers.Serializer):
    uuid = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=150)

class ListItemSerializer(serializers.Serializer):
    uuid = serializers.UUIDField(read_only=True)
    quantity = serializers.IntegerField(default=1, min_value=1)
    item = ItemSerializer()

    # class Meta:
    #     model = ListItem
    #     fields = ['uuid', 'item', 'list', 'quantity']

class DetailedListSerializer(serializers.Serializer):
    uuid = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=150)
    items = ListItemSerializer(many=True, read_only=True)