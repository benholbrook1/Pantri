
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import List
from .serializers import ListSerializer, DetailedListSerializer

# Create your views here.

@api_view()
def lists(request):
    listQueryset = List.objects.all()
    serializer = ListSerializer(listQueryset, many=True)
    return Response(serializer.data)

@api_view()
def lists_detail(request, id):

    list = get_object_or_404(List, pk=id)
    serializer = DetailedListSerializer(list)
    return Response(serializer.data)
   