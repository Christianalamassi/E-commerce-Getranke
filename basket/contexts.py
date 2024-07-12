from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from drinks.models import Drink


def your_order(request):

    basket_drink = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for basket_id, item_data in basket.items():
        if isinstance(item_data, int):
            drink = get_object_or_404(Drink, pk=basket_id)
            total += item_data * drink.price
            product_count += item_data
            basket_drink.append({
                'basket_id': basket_id,
                'quantity': item_data,
                'drink': drink,
            })
        else:
            drink = get_object_or_404(Drink, pk=basket_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * drink.price
                product_count += quantity
                basket_drink.append({
                    'basket_id': basket_id,
                    'quantity': quantity,
                    'drink': drink,
                })
    context = {
        'basket_drink': basket_drink,
        'total': total,
        'product_count': product_count,
    }

    return context
