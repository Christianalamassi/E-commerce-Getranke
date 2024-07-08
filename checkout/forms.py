from django import forms
from .models import CheckOut


class CheckOutForm(forms.ModelForm):
    class Meta:
        """
        which model the form reffers to and which fields
        from the model will be render
        """
        model = CheckOut
        fields = (
            'full_name',
            'email',
            'phone_number',
            'street_address',
            'postcode',
            'state',
            'note',
            )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """

        super().__init__(*args, **kwargs)
        # here is the placeholders will view in inputs
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'street_address': 'Street Address',
            'state':'City',
            'postcode': 'Postal Code',
            'note':'Type here your notification....(Optional)'
        }

        # sets autofocus on full name field
        self.fields['full_name'].widget.attrs['autofocus'] = True

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]}'

            # sets attributes for place holder and class and removes labels
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False

