from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'name', 'email', 'message'
        ]

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """

        super().__init__(*args, **kwargs)
        # here is the placeholders will view in inputs
        placeholders = {
            'name': 'Full name',
            'email': 'example@example.com',
            'message': 'Enter your question here.......'
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]}'

            # sets attributes for place holder and class and removes labels
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
