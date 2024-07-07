from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import CheckOut


@login_required
def profile(request):
    """ 
    Display the user's profile.
    allows the users to request
    displays an individual instance model:`.UserProfile`
    **Context**
    ``UserProfile``
    the most recent instence model:`.UserProfile`
    ``UserProfileForm``
    an instence of form:`.UserProfileForm`
    **redirect**
    an instence of view :`profiles.profile`
    **Template**
    templat:`profiles/profile.html`
    """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method =='POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully")
        else:
            messages.error(request, "Somthing went wrong")
    else:
        form = UserProfileForm(instance=profile)
    orders= profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile':True,
        }

    return render(request, template, context)

def order_details(request, order_number):
    """ render checkout_success page"""

    order = get_object_or_404(CheckOut, order_number=order_number)

    messages.info(request, (
        f'This is an old confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))


    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile':True,
        }

    return render(request, template, context)