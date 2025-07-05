from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer

# Create your views here.

@api_view()
def item_list(request):
    itemQueryset = Item.objects.all()
    serializer = ItemSerializer(itemQueryset, many=True)
    return Response(serializer.data)

@api_view()
def item_detail(request, id):

    item = get_object_or_404(Item, pk=id)
    serializer = ItemSerializer(item)
    return Response(serializer.data)
   