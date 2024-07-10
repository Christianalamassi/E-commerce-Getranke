from django import forms
from .models import HowMuchLike


class HowMuchLikeForm(forms.ModelForm):

    class Meta:
        model = HowMuchLike
        fields = [
            'like','feedback'
        ]

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """

        super().__init__(*args, **kwargs)
        # here is the placeholders will view in inputs
        placeholders = {
            'like': '',
            'feedback':'Enter you type here.......'
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]}'

            # sets attributes for place holder and class and removes labels
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False


