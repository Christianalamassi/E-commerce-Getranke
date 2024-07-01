from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import CheckOutForm
from .models import CheckOut, CheckOutLineItem
from drinks.models import Drink
from basket.contexts import your_order

import stripe
import json


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """

        intent = event.data.object
        pid = intent.id
        basket = intent.metadata.basket
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details # updated
        shipping_details = intent.shipping
        total = round(stripe_charge.amount / 100, 2) # updated

        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[Faild] = None
            
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = CheckOut.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    postcode__iexact=shipping_details.address.postal_code,
                    state__iexact=shipping_details.address.state,
                    street_address__iexact=shipping_details.address.line1,
                    total=total,
                    original_basket=basket,
                    stripe_pid=pid
                )

                order_exists = True
                break
            except CheckOut.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = CheckOut.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_numbet=shipping_details.phone,
                    postcode=shipping_details.address.postal_code,
                    state=shipping_details.address.state,
                    street_address1=shipping_details.address.line,
                    total=total,
                    original_basket=basket,
                    stripe_pid=pid
                )
                for basket_id, item_data in json.loads(basket).items():
                    drink = Drink.objects.get(id=basket_id)
                    if isinstance(item_data, int):
                        order_line_item = CheckOutLineItem(
                            order=order,
                            drink=drink,
                            quantity=item_data,
                        )
                        order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
        return HttpResponse(
            content=f'Faild Webhook received: {event["type"]}',
            status=200)
