from django.contrib import admin
from .models import ToPay, ToPayLineItem 


class ToPayLineItemAdminInline(admin.TabularInline):
    model = ToPayLineItem
    readonly_fields = ('lineitem_total',)


class ToPayAdmin(admin.ModelAdmin):

    inlines = (ToPayLineItemAdminInline,)

    readonly_fields= (
        'order_number',
        'states',
        'date' ,
        'order_total',
    )

    fields = (
    'order_number',
    'full_name',
    'email',
    'phone_number', 
    'states',
    'postcode',
    'street_address1',
    'street_address2',
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

admin.site.register(ToPay,ToPayAdmin)