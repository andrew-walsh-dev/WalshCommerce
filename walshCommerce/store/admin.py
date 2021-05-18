from django.contrib.auth import models
from store.models import Product
from django.contrib import admin


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')

admin.site.register(Product, ProductAdmin)