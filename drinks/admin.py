from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    lsit_display = (
        'name',
        'price',
        'rating',
        'image',
    )
    ordering = ('price', )

admin.site.register(Product)
