from rest_framework import serializers
from .models import Ecommerce

class EcommerceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ecommerce
        fields = ['product_id', 'product_name', 'price', 'description']
