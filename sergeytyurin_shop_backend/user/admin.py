from django.contrib import admin

from .models import Client, ClientDeliveryInformation

admin.site.register(Client)
admin.site.register(ClientDeliveryInformation)
