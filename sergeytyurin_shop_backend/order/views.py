from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Order
from .serializers import OrderSerializer


class LatestOrderList(APIView):
    def get(self, request, format=None):
        products = Order.objects.filter()
        serializer = OrderSerializer(products, many=True)
        return Response(serializer.data)