from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import CheckOutForm
from .models import CheckOut, CheckOutLineItem
from drinks.models import Drink
from basket.contexts import your_order
from profiles.models import UserProfile
from profiles.forms import UserProfileForm

import stripe
import json


@require_POST
def cache_checkout_data(request):

    """
    handles if user wants to save details of the payment
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, "Sorry, We couldn't procsses your pyment now.\
            Please try again later.")
        return HttpResponse(content=e, status=400)


def checkout(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        basket = request.session.get('basket', {})

        form_data  = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address': request.POST['street_address'],
            'postcode': request.POST['postcode'],
            'state': request.POST['state'],
            }
        check_out = CheckOutForm(form_data)
        if check_out.is_valid():
            order=check_out.save(commit=False)
            pid=request.POST.get('client_secret').split('_secret')[0]
            order_stripe_pid = pid
            order_original_basket=json.dumps(basket)
            order.save
            order = check_out.save()
            for basket_id, item_data in basket.items():
                try:
                    drink = Drink.objects.get(id=basket_id)
                    if isinstance(item_data, int):
                        order_line_item = CheckOutLineItem(
                            order=order,
                            drink=drink,
                            quantity=item_data,
                        )
                        order_line_item.save()

                except Drink.DoesNotExist:
                    messages.error(request, (
                        "One of the drink in your basket wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('basket'))

            # Save the info to the user's profile if all is well
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please check your information again.')
            
    else:
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request, 'Your basket is empty')
            return redirect(reverse('drinks'))

        your_orders = your_order(request)
        total = your_orders['total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    check_out = CheckOutForm()
    template = 'checkout/checkout.html'
    context = {
        'check_out':check_out,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret
    }

    return render(request, template, context)



def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(CheckOut, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_street_address': order.street_address,
                'default_postcode': order.postcode,
                'default_state': order.state,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Your order has been successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)