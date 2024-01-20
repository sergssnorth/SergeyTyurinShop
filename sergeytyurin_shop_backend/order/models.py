from django.db import models
from django.contrib.auth.models import User
from user.models import ClientDeliveryInformation

from product.models import Product

    
class OrderStatus(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return '%s' % self.id
    

class Order(models.Model):
    client_delivery_information = models.ForeignKey(ClientDeliveryInformation, related_name='orders', on_delete=models.CASCADE)
    order_status = models.ForeignKey(OrderStatus, related_name='orders', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True)

    class Meta:
        ordering = ['-created_at',]
    
    def __str__(self):
        return self.first_name
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return '%s' % self.id