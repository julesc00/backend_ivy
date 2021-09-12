from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import (Product, Review, Order, OrderItem, ShippingAddress)
from .serializers import ProductSerializer


@api_view(["GET"])
def list_products(request):
    """Listing products"""
    products = Product.objects.all().order_by("-createdAt")
    serializer = ProductSerializer(products, many=True)

    return Response(serializer.data)


@api_view(["GET"])
def get_product(request, pk):
    product = Product.objects.filter(_id=pk).first()
    serializer = ProductSerializer(product, many=False)

    return Response(serializer.data)
