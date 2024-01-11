from django.shortcuts import render
from.models import Product,ProductDiscount
from.serializers import Productserializer,DiscountSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET','POST'])
def Product_data(request):
    if request.method=='GET':
        prod=Product.objects.all()
        serializer=Productserializer(prod,many=True)
        return JsonResponse(serializer.data,status=status.HTTP_202_ACCEPTED,safe=False)
    if request.method=='POST':
        serializer=Productserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def Product_details(request,id):
    try:
        prod=Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=Productserializer(prod)
        return JsonResponse(serializer.data)
    elif request.method=='PUT':
        serializer=Productserializer(prod,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        prod.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST','GET','PUT','DELETE'])
def product_discount(request):
    if request.method=='POST':
        serializer=DiscountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    #return Response(status=status.HTTP_201_CREATED)

    elif request.method=='GET':
        discount_products=ProductDiscount.objects.all()
        serializer =DiscountSerializer(discount_products,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method=='PUT':
        discount_products = ProductDiscount.objects.get(prodname=request.data['prodname'])
        serializer=DiscountSerializer(discount_products,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method=='DELETE':
        discount_products = ProductDiscount.objects.get(prodname=request.data['prodname'])
        discount_products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)