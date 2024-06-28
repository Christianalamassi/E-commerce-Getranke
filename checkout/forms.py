from django import forms
from .models import ToPay


class CheckOutForm(forms.ModelForm):
    class Meta:
        """
        which model the form reffers to and which fields
        from the model will be render
        """
        model = ToPay
        fields = (
           'full_name',
            'email',
            'phone_number',
            'street_address1',
            'street_address2',
            'state',
            'postcode',
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
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'state':'State',
            'postcode': 'Postal Code',
        }

        # sets autofocus on full name field
        self.fields['full_name'].widget.attrs['autofocus'] = True

        for field in self.fields:
            placeholder = placeholders[field]

            # sets attributes for place holder and class and removes labels
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False

