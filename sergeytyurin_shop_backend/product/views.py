from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

from .models import Product, Category, ClientDeliveryInformation, Client
from .serializers import ProductSerializer, CategorySerializer, UserTokenSerializer, ClientDeliveryInformationSerializer, ClientSerializer

class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.filter()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    
class CategoryProductsList(APIView):
    def get(self, request, big_category_slug, category_slug, format=None):
        products = Product.objects.filter(category__big_category__slug = big_category_slug).filter(category__slug = category_slug)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get(self, request, big_category_slug, category_slug, product_slug, format=None):
        product = Product.objects.filter(category__big_category__slug = big_category_slug).filter(category__slug = category_slug).get(slug = product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
class CategoriesList(APIView):
    def get(self, request, big_category_slug, format=None):
        products = Category.objects.filter(big_category__slug = big_category_slug)
        serializer = CategorySerializer(products, many=True)
        return Response(serializer.data)
    

class UserIdDetail(APIView):
    def get(self, request, token, format=None):
        user_information = Token.objects.filter(key = token)
        serializer = UserTokenSerializer(user_information, many = True)
        return Response(serializer.data)
    
class ClientInformationDetail(APIView):
    def get(self, request, user_id, format=None):
        user_information = Client.objects.filter(user_id = user_id)
        serializer = ClientSerializer(user_information, many=True)
        return Response(serializer.data)