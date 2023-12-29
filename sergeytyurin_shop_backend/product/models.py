from django.core.files import File
from django.db import models
from django.contrib.auth.models import User

BASE_BACKEND_URL = 'http://127.0.0.1:8000'

class BigCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('id',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'
    

class Category(models.Model):
    big_category = models.ForeignKey(BigCategory, related_name='categorys', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.big_category.slug}/{self.slug}/'


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image1 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    image2 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    image3 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    image4 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/product/{self.category.big_category.slug}/{self.category.slug}/{self.slug}/'
    
    def get_image1(self):
        if self.image1:
            # return('http://127.0.0.1:8000' + self.image1.url)
            return(BASE_BACKEND_URL + self.image1.url)
        else: 
            return ''
        
    def get_image2(self):
        if self.image2:
            # return('http://127.0.0.1:8000' + self.image2.url)
            return(BASE_BACKEND_URL + self.image2.url)
        else: 
            return ''
        
    def get_image3(self):
        if self.image3:
            # return('http://127.0.0.1:8000' + self.image3.url)
            return(BASE_BACKEND_URL + self.image3.url)
        else: 
            return ''
        
    def get_image4(self):
        if self.image4:
            # return('http://127.0.0.1:8000' + self.image4.url)
            return(BASE_BACKEND_URL + self.image4.url)
        else: 
            return ''

class ProductSize(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField()

    class Meta:
        ordering = ('id',)
        verbose_name = "Размер одежды"
        verbose_name_plural = "Размеры одежды"
    
    def __str__(self):
        return self.name
        
class AvailableProductSize(models.Model):
    product = models.ForeignKey(Product, related_name='available_product_size', on_delete=models.CASCADE)
    size = models.ForeignKey(ProductSize, on_delete=models.CASCADE)

    class Meta:
        ordering = ('size',)
    
    def __str__(self):
        return f'{self.product.name} - {self.size.name}'

    def size_slug(self):
        return self.size.slug
    
    def size_name(self):
        return self.size.name
    

