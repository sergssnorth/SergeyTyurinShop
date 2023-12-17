from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Client(models.Model):
    user = models.ForeignKey(User, related_name='client_information', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    sname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)

    class Meta:
        ordering = ('user',)
    
    def __str__(self):
        return f'{self.user.username}'

class ClientDeliveryInformation(models.Model):
    client = models.ForeignKey(Client, related_name='client_delivery_information', on_delete=models.CASCADE)
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    building = models.CharField(max_length=100)

    class Meta:
        ordering = ('client',)
    
    def __str__(self):
        return f'{self.client.user.username}'