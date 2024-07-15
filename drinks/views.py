from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Drink, Alcohol
from .forms import DrinkForm


def all_drink(request):
    """
    A view to show all kind of drinks, including sorting and search queries
    allows the users to receive.
    displays an individual instance model:`.Alcohol, .Drink`
    **Context**
    ``Alcohol``,``Drink``
    the most recent instence model:`.Alkohol, .Drink`
    ``DrinkForm``
    an instence of form:`.DrinkForm`
    **redirect**
    an instence of view :`drinks.drinks`
    **Template**
    templat:`drinks/drinks.html`
    """

    drinks = Drink.objects.all()
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                messages.error(request, 'Error entered search term')
                return redirect(reverse('drinks'))
            queries = Q(name__icontains=query)
            drinks = drinks.filter(queries)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                drinks = drinks.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'descending':
                    sortkey = f'-{sortkey}'
            drinks = drinks.order_by(sortkey)

    sorting_by = f'{sort}_{direction}'

    context = {
        'drinks': drinks,
        'search_term': query,
        'sorting_by': sorting_by,
    }
    return render(request, "drinks/drinks.html", context)


def each_drink(request, drink_id):
    """
    A view to show each drink's details individual
    allows the users to receive
    displays an individual instance model:`.Drink, Alcohol`
    **Context**
    ``Drink``,``Alcohol``
    the most recent instence model:`.Drink`
    ``DrinkForm``
    an instence of form:`.DrinkForm`
    **redirect**
    an instence of view :`drinks.each_drink`
    **Template**
    templat:`drinks/each_drink.html`
    """

    drink = get_object_or_404(Drink, pk=drink_id)
    context = {
        'drink': drink
    }
    return render(request, "drinks/each_drink.html", context)


@login_required
def add_drink(request):
    """Add a drink to the shop"""

    if not request.user.is_superuser:
        messages.error(request, 'Danger. You are not allowed to do this')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = DrinkForm(request.POST, request.FILES)
        if form.is_valid():
            drink = form.save()
            messages.success(request, "You added it successfully")
            return redirect(reverse('each_drink', args=[drink.id]))
        else:
            messages.error(request, "Somthing went wrong, try again")
    else:
        form = DrinkForm()
    template = 'drinks/add_drink.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_drink(request, drink_id):
    """Update a drink to the shop"""

    if not request.user.is_superuser:
        messages.error(request, 'Danger. You are not allowed to do this')
        return redirect(reverse('home'))

    drink = get_object_or_404(Drink, pk=drink_id)
    if request.method == "POST":
        form = DrinkForm(request.POST, request.FILES, instance=drink)
        if form.is_valid():
            form.save()
            messages.success(request, "You edited it successfully")
            return redirect(reverse('each_drink', args=[drink.id]))
        else:
            messages.error(request, "Somthing went wrong, try again")
    else:
        form = DrinkForm(instance=drink)
        messages.info(request, f"You are making a change in {drink.name}")

    template = 'drinks/edit_drink.html'
    context = {
        'form': form,
        'drink': drink,
    }
    return render(request, template, context)


@login_required
def delete_drink(request, drink_id):
    """ Admin deletion products"""

    if not request.user.is_superuser:
        messages.error(request, 'Danger. You are not allowed to do this')
        return redirect(reverse('home'))

    drink = get_object_or_404(Drink, pk=drink_id)
    drink.delete()
    messages.success(request, f"You removed {drink.name} from the offer")
    return redirect(reverse('drinks'))
