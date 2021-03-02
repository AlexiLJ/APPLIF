from rest_framework import serializers
from api.models import Product, Offer


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
    offers = OfferSerializer()