from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from .models import News
from .forms import NewsForm

# Create your views here.

def index(request):
    """ A view to the main page of the project """

    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,("You have been applied for the newsletter successfully."))
        else:
            messages.error(request, ("This email is not registered with our website."))
    form = NewsForm()
    context = {
        'form': form
    }
    return render(request, 'mainapp/index.html', context)
