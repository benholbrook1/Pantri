from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def item_list(request):
    if request.method == 'GET':
        itemQueryset = Item.objects.all()
        serializer = ItemSerializer(itemQueryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.validated_data['created_by'] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view()
def item_detail(request, id):
    item = get_object_or_404(Item, pk=id)
    serializer = ItemSerializer(item)
    return Response(serializer.data)
   