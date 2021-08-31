from rest_framework import serializers

from .models import (Product, Order, OrderItem, Review, ShippingAddress)


class ProductSerializer(serializers.ModelSerializer):
    """Serialize the Product object."""

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ("id", "_id")
