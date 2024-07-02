from django.contrib import admin
from .models import CheckOut, CheckOutLineItem 


class CheckOutLineItemAdminInline(admin.TabularInline):
    model = CheckOutLineItem
    readonly_fields = ('lineitem_total',)


class CheckOutAdmin(admin.ModelAdmin):

    inlines = (CheckOutLineItemAdminInline,)

    readonly_fields= (
        'order_number',
        'states',
        'date' ,
        'order_total',
    )

    fields = (
    'order_number',
    'user_profile'
    'full_name',
    'email',
    'phone_number', 
    'states',
    'postcode',
    'street_address',
    'date',
    'order_total',
    'total',
    'original_basket',
    'stripe_pid',
)

    display = (
        'order_number',
        'full_name',
        'email',
        'states',
    )

    ordring =('-data',)

admin.site.register(CheckOut,CheckOutAdmin)