from django.shortcuts import render, get_object_or_404

from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import CheckOut


def profile(request):
    """ Display the user's profile. """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request =='POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messgaes.success=(request, "Your profile has been updated successfully")
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

def order_details(requesdt, order_number):
    order = get_object_or_404(CheckOut, oreder_number=order_number)

    messages.info(request, (
        f'This is an old confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

   
    template = 'checkout/scheckout_success.html'
    context = {
        'orders': orders,
        'from_profile':True,
        }

    return render(request, template, context)