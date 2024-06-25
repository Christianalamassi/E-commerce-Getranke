from django.shortcuts import render
from .models import Product

# Create your views here.

def drinks(request):
    """ A view to show all kind of drinks, including sorting and search queries """

    drinks = Product.objects.all()
    context = {
        'drinks': drinks
    }
    return render(request, "drinks/drinks.html", context)