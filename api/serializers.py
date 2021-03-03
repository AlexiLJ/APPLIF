from rest_framework import serializers
from api.models import Product, Offer


class OfferSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Offer
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Product
        fields = ["id", "name", "description", "offers"]
        depth = 1
