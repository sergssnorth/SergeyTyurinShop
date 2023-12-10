from django.contrib import admin

from .models import Category, Product, BigCategory

admin.site.register(BigCategory)
admin.site.register(Category)
admin.site.register(Product)
