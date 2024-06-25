from django.shortcuts import render, get_object_or_404
from .models import Product
from django.contrib import messages
from django.db.models import Q

# Create your views here.

def drinks(request):
    """ A view to show all kind of drinks, including sorting and search queries """
    
    drinks = Product.objects.all()
    qurey = None

    if request.GET:
        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                message.error('Enter keyword')
                return redirect(reverse, ('drinks'))
        queries = Q(name__icontains = query)
        drinks = drinks.filter(queries)
    context = {
        'drinks': drinks,
        'querys':query
    }
    return render(request, "drinks/drinks.html", context)

def each_drink(request, drink_id):
    """ A view to show each drink's details individual """

    drink = get_object_or_404(Product, pk=drink_id)
    context = {
        'drink': drink
    }
    return render(request, "drinks/each_drink.html", context)