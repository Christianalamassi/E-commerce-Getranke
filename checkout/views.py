from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import CheckOutForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, 'Your basket is empty')
        return redirect(reverse('drinks'))

    checkout_form = CheckOutForm()
    template = checkout/checkout.html
    context = {
        'checkout_form':checkout_form,
        'strip_public_key': 'pk_test_51PUXLlP1KEXrqREgl7cpr8yRBXeUopaozkOqMBo5JcZT34QBPh844Uc6QWEEYg1tOuBgBaqFrVegs71FpVgYYwx100ntcnqiI3',
        'clinet_secret': 'text'
    }
    return render(request, template, context)