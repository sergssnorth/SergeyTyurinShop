from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Client, ClientDeliveryInformation



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


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = (
            "key",
            "user_id",
        )

