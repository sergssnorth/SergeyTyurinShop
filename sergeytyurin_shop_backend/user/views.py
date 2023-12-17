from django.shortcuts import render

from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view


from rest_framework.authtoken.models import Token
from .models import ClientDeliveryInformation, Client
from .serializers import  UserTokenSerializer, ClientDeliveryInformationSerializer, ClientSerializer

# Create your views here.

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
    