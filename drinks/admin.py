from django.contrib import admin
from .models import Drink, Alcohol


class DrinkAdmin(admin.ModelAdmin):
    lsit_display = (
        'name',
        'price',
        'rating',
        'image',
    )
    ordering = ('price', )


class AlcoholAdmin(admin.ModelAdmin):
    lsit_display = (
        'name'
    )


admin.site.register(Drink)
admin.site.register(Alcohol)
