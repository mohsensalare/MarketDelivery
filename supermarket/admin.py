from django.contrib import admin
from supermarket.models import Product, SuperMarket, ProductGallery, Category

# Register your models here.

admin.site.register(Product)
admin.site.register(SuperMarket)
# admin.site.register(ProductGallery)
admin.site.register(Category)