from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import News
from .forms import NewsForm


def index(request):
    """ A view to the main page of the project """

    return render(request, "mainapp/index.html")

def news(request):
    """ Users newslater update"""

    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"You have been applied for the newsletter successfully")
            return redirect('index')

    form = NewsForm()
    context = {
        'form': form
    }
    messages.error(request, "Somthing went wrong, try again")
    return render(request, 'mainapp/index.html', context)
