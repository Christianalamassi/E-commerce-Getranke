from django.shortcuts import get_object_or_404
from drinks.models import Drink
from django.conf import settings


def your_order(request):

    basket_order = []
    total = 0
    number_of_drinks= 0
    bag = request.session.get('bag', {})

    for basket_id, quantity in bag.items():
        drink = get_object_or_404(Drink, pk=basket_id)
        total += quantity * drink.price
        number_of_drinks += quantity
        basket_order.append({
            'basket_id': basket_id,
            'quantity': quantity,
            'drink': drink
            })

    context  ={
        'basket_order': basket_order,
        'total': total,
        'number_of_drinks': number_of_drinks,
    }
    return context
