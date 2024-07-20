from django.shortcuts import render, reverse, get_object_or_404
from django.contrib import messages
from .models import Question
from .forms import QuestionForm


def question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "We received your question, \
            We will get back to you as soon as possible")
        else:
            messages.error(request, ("This email is invalid."))
    form = QuestionForm()
    context = {
        'form': form
    }
    return render(request, 'contacts/question.html', context)
