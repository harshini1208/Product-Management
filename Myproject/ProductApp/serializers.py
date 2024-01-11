from rest_framework import serializers
from.models import Product,ProductDiscount


class Productserializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductDiscount
        fields=['id','prodname','pdiscount']
