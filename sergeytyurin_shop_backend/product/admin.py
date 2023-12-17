from django.contrib import admin

from .models import Category, Product, BigCategory, ProductSize, AvailableProductSize

admin.site.register(BigCategory)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductSize)
admin.site.register(AvailableProductSize)