from django.shortcuts import get_object_or_404
from rest_framework import status, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Good
from .serializers import GoodSerializer

# Create your views here. 
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/goods',
        'Search by Category': '/?category=category_name',
        'Search by Subcategory': '/?subcategory=category_name',
        'Add': 'goods/add/',
        'Update': '/update/pk',
        'Delete': '/goods/pk/delete'
    }
            
    return Response(api_urls)

@api_view(['POST'])
def add_good(request):
   serializer = GoodSerializer(data=request.data)
   
   if Good.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
   
   if serializer.is_valid():
       serializer.save()
       return Response(serializer.data, status=status.HTTP_201_CREATED)
   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_goods(request):
    goods = Good.objects.all()
    serializer = GoodSerializer(goods, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_good_by_id(request, pk):
    good = get_object_or_404(Good, pk=pk)
    good.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['PATCH'])
def update_good_by_id(request, pk):
    good = get_object_or_404(Good, pk=pk)
    serializer = GoodSerializer(good, data=request.data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)