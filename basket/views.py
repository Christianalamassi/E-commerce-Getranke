from django.shortcuts import render,redirect, reverse, get_object_or_404
from django.contrib import messages
from drinks.models import Drink


def basket(request):
    """ A view that renders the basket """

    return render(request, 'basket/basket.html')


def add_basket(request, basket_id):
    """ Add a more to the basket """

    drink = Drink.objects.get(pk = basket_id)
    numbers = float(request.POST.get('numbers'))
    redirect_url = request.POST.get('redirect_url')
    in_basket = request.session.get('in_basket', {})

    if basket_id in list(in_basket.keys()):
        in_basket[basket_id] += numbers
        messages.success(request, 'The order has been updated')
    else:
        in_basket[basket_id] = numbers
        messages.success(request, 'The order has been added')
    request.session['in_basket'] = in_basket

    return redirect(redirect_url)


def fix_basket(request, basket_id):
    """ Edit the basket """

    drink = get_object_or_404(Drink, pk=basket_id)
    numbers = float(request.POST.get('numbers'))
    in_basket = request.session.get('in_basket', {})

    if quantity > 0:
        bag[basket_id] = numbers
        messages.success(request, 'The order has been updated')
    else:
        in_basket.pop(basket_id)
        messages.success(request, 'Your order has be deleted')

    request.session['in_basket'] = in_basket
    return redirect(reverse('basket'))


def delete_order(request, basket_id):
    """Delete the order from the basket"""

    try:
        drink = get_object_or_404(Drink, pk=basket_id)

        in_basket = request.session.get('in_basket', {})

        in_basket.pop(basket_id)
        messages.success(request, f'Your order has be deleted')

        request.session['in_basket'] = in_basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error deleting your order: {e}')
        return HttpResponse(status=500)