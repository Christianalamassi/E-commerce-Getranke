from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import HowMuchLike
from .forms import HowMuchLikeForm


@login_required
def likes(request):
    """Render the page where the user can submit their feedback"""

    if request.method == 'POST':
        form = HowMuchLikeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for sharing your opinion.")
            return redirect('home')
        else:
            messages.ERROR(request, "Something went wrong, Try again")
    form = HowMuchLikeForm()
    context = {
        'form': form
    }
    return render(request, "likes/likes.html", context)
