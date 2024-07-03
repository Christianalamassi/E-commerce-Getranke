from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .forms import CheckOutForm
from .models import CheckOut, CheckOutLineItem
from drinks.models import Drink
from profiles.models import UserProfile
from basket.contexts import your_order

import stripe
import json
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):

        """Send the user a confirmation email"""
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})
        
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )        

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

        intent = event.data.object
        pid = intent.id
        basket = intent.metadata.basket
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[Faild] = None

        # Update profile information if save_info was checked
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = shipping_details.phone
                profile.default_street_address = shipping_details.address.line
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_state= shipping_details.address.city
                profile.save()
            
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
                    street_address__iexact=shipping_details.address.line,
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
            self.__send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = CheckOut.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_numbet=shipping_details.phone,
                    street_address=shipping_details.address.line,
                    postcode=shipping_details.address.postal_code,
                    state=shipping_details.address.state,
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
        self.__send_confirmation_email(order)
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


        

