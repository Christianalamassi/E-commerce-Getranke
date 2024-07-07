from django.shortcuts import render,redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from drinks.models import Drink



def basket(request):
    """ A view that renders the basket """

    return render(request, 'basket/basket.html')


def add_basket(request, basket_id):
    """ Add a more to the basket """

    drink = get_object_or_404(Drink, pk=basket_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if basket_id in list(basket.keys()):
        basket[basket_id] += quantity
        messages.success(request, f'Updated {drink.name} quantity to {basket[basket_id]}')
    else:
        basket[basket_id] = quantity
        messages.success(request, f'Added {drink.name} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)
    

def fix_basket(request, basket_id):
    """Adjust the quantity of the specified product to the specified amount"""

    drink = get_object_or_404(Drink, pk=basket_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})


    if quantity > 0:
        basket[basket_id] = quantity
        messages.success(request, f'Updated {drink.name} quantity to {basket[basket_id]}')
    else:
        basket.pop(basket_id)
        messages.success(request, f'Removed {drink.name} from your basket')

    request.session['basket'] = basket
    return redirect(reverse('basket'))


def remove(request, basket_id):
    """Remove the drink from the basket"""

    try:
        drink = get_object_or_404(Drink, pk=basket_id)
        basket = request.session.get('basket', {})

        basket.pop(basket_id)
        messages.success(request, f'Removed {drink.name} from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing the drink: {e}')
        return HttpResponse(status=500)