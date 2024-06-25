from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to the main page of the project """

    return render(request, "mainapp/index.html")