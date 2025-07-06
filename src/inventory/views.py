from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Item
from .serializers import ItemSerializer

# Create your views here.

class ItemList(APIView):
    def get(self, request):
        itemQueryset = Item.objects.all()
        serializer = ItemSerializer(itemQueryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.validated_data['created_by'] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET', "PATCH", "DELETE"])
def item_detail(request, id):
    item = get_object_or_404(Item, pk=id)
    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        serializer = ItemSerializer(item, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK) 
    elif request.method == 'DELETE':
        item.is_active = False
        item.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
   