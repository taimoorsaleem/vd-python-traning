from rest_framework import serializers
from .models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    price = serializers.IntegerField(write_only=True)
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field='id')

    class Meta:
        model = Product
        fields = serializers.ALL_FIELDS

    def validate_price(self, price):
        if price > 0:
            return price
        else:
            raise serializers.ValidationError(
                'Price must be greater than zero.')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = serializers.ALL_FIELDS
