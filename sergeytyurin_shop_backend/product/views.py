from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.filter()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get(self, request, big_category_slug, category_slug, product_slug, format=None):
        
        # products = Product.objects.filter(big_category_slug).filter(category_slug).filter(slug = product_slug)
        products = Product.objects.filter(category__big_category__slug = big_category_slug).filter(category__slug = category_slug).get(slug = product_slug)
        serializer = ProductSerializer(products)
        return Response(serializer.data)
    
