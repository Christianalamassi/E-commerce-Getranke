from django.shortcuts import get_object_or_404
from decimal import Decimal
from django.conf import settings
from drinks.models import Drink


def your_order(request):

    basket_order = []
    total = 0
    number_of_drinks= 0
    in_basket = request.session.get('in_basket', {})

    for basket_id, quantity in in_basket.items():
        drink = get_object_or_404(Drink, pk=basket_id)
        total += quantity * float(drink.price)
        number_of_drinks += quantity
        basket_order.append({
            'basket_id': basket_id,
            'quantity': int(quantity),
            'drink': drink
            })

    context  ={
        'basket_order': basket_order,
        'total': total,
        'number_of_drinks': number_of_drinks,
    }
    return context