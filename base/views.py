from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .products import products


@api_view(["GET"])
def list_products(request):
    return Response(products)


@api_view(["GET"])
def get_product(request, pk):
    product = [item for item in products if item.get("_id") == pk]

    return Response(product)
