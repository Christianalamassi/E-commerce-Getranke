from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from drinks.models import Drink


def your_order(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            drink = get_object_or_404(Drink, pk=item_id)
            total += item_data * drink.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'drink': drink,
            })
        else:
            drink = get_object_or_404(Drink, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * drink.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'drink': drink,
                    'size': size,
                })
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
    }

    return context