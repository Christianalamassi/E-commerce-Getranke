from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import CheckOutForm
from basket.contexts import your_order

import stripe


def checkout(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    basket = request.session.get('basket', {})
    # if not basket:
    #     messages.error(request, 'Your basket is empty')
    #     return redirect(reverse('drinks'))

    # your_orders = your_order(request)
    # totals = your_order['total']
    #stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    checkout_form = CheckOutForm()
    template = 'checkout/checkout.html'
    context = {
        'checkout_form':checkout_form,
        'strip_public_key': 'stripe_public_key',
        'client_secret': 'intent.client_secret'
    }

    return render(request, template, context)