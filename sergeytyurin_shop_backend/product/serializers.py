from rest_framework import serializers

from .models import BigCategory, Category, Product, AvailableProductSize, ProductSize, Client, ClientDeliveryInformation
from rest_framework.authtoken.models import Token


class ProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = (
            "name",
            "slug",
        )


class AvailableProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableProductSize
        fields = (
            "size_name",
            "size_slug",
        )



class ProductSerializer(serializers.ModelSerializer):
    available_product_size = AvailableProductSizeSerializer(many=True)
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "price",
            "get_image1",
            "get_image2",
            "get_image3",
            "get_image4",
            "available_product_size",
        )

class BigCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BigCategory
        fields = (
            "id",
            "slug",
        )


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Category
        fields = (
            "big_category",
            "id",
            "name",
            "get_absolute_url",
            "products",
        )

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = (
            "key",
            "user_id",
        )


class ClientDeliveryInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientDeliveryInformation
        fields = (
            "region",
            "city",
            "street",
            "building",
        )



class ClientSerializer(serializers.ModelSerializer):
    client_delivery_information = ClientDeliveryInformationSerializer(many=True)
    class Meta:
        model = Client
        fields = (
            "client_delivery_information",
            "name",
            "sname",
            "email",
            "phone",
        )
