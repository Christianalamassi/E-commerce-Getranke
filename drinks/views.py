from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def drinks(request):
    """ A view to show all kind of drinks, including sorting and search queries """

    drinks = Product.objects.all()
    context = {
        'drinks': drinks
    }
    return render(request, "drinks/drinks.html", context)

def each_drink(request, drink_id):
    """ A view to show each drink's details individual """

    drink = get_object_or_404(Product, pk=drink_id)
    context = {
        'drink': drink
    }
    return render(request, "drinks/each_drink.html", context)