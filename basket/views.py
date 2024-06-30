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
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if basket_id in list(bag.keys()):
            if size in bag[basket_id]['items_by_size'].keys():
                bag[basket_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()} {drink.name} quantity to {bag[item_id]["items_by_size"][size]}')
            else:
                bag[basket_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {drink.name} to your bag')
        else:
            bag[basket_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {drink.name} to your bag')
    else:
        if basket_id in list(bag.keys()):
            bag[basket_id] += quantity
            messages.success(request, f'Updated {drink.name} quantity to {bag[basket_id]}')
        else:
            bag[basket_id] = quantity
            messages.success(request, f'Added {drink.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)
    

def fix_basket(request, basket_id):
    """Adjust the quantity of the specified product to the specified amount"""

    drink = get_object_or_404(Drink, pk=basket_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[basket_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {drink.name} quantity to {bag[item_id]["items_by_size"][size]}')
        else:
            del bag[basket_id]['items_by_size'][size]
            if not bag[basket_id]['items_by_size']:
                bag.pop(basket_id)
            messages.success(request, f'Removed size {size.upper()} {drink.name} from your bag')
    else:
        if quantity > 0:
            bag[basket_id] = quantity
            messages.success(request, f'Updated {drink.name} quantity to {bag[basket_id]}')
        else:
            bag.pop(basket_id)
            messages.success(request, f'Removed {drink.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('basket'))


def remove(request, basket_id):
    """Remove the drink from the basket"""

    try:
        drink = get_object_or_404(Drink, pk=basket_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[basket_id]['items_by_size'][size]
            if not bag[basket_id]['items_by_size']:
                bag.pop(basket_id)
            messages.success(request, f'Removed size {size.upper()} {drink.name} from your bag')
        else:
            bag.pop(basket_id)
            messages.success(request, f'Removed {drink.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)