from django.shortcuts import render,redirect, reverse


def basket(request):
    """ A view that renders the basket """

    return render(request, 'basket/basket.html')


def add_basket(request, basket_id):
    """ Add a more to the basket """

    numbers = float(request.POST.get('numbers'))
    redirect_url = request.POST.get('redirect_url')
    in_basket = request.session.get('in_basket', {})

    if basket_id in list(in_basket.keys()):
        in_basket[basket_id] += numbers
    else:
        in_basket[basket_id] = numbers

    request.session['in_basket'] = in_basket

    return redirect(redirect_url)


def fix_basket(request, basket_id):
    """ Edit the basket """

    numbers = float(request.POST.get('numbers'))
    in_basket = request.session.get('in_basket', {})

    if basket_id in list(in_basket.keys()):
        in_basket[basket_id] += numbers
    else:
        in_basket[basket_id] = numbers

    request.session['in_basket'] = in_basket
    print('Delete')
    return redirect(reverse('basket'))
