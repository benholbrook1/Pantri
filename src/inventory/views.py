from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Item
from .serializers import ItemSerializer

# Create your views here.

class ItemList(APIView):
    def get(self, request):
        itemQueryset = Item.objects.filter(is_active=True)
        serializer = ItemSerializer(itemQueryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.validated_data['created_by'] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

class ItemDetail(APIView):
    def get(self, request, id):
        item = get_object_or_404(Item, pk=id)
        serializer = ItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, id):
        item = get_object_or_404(Item, pk=id)
        serializer = ItemSerializer(item, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK) 

    def delete(self, request, id):
        item = get_object_or_404(Item, pk=id)
        item.is_active = False
        item.save()
        return Response(status=status.HTTP_204_NO_CONTENT)



   