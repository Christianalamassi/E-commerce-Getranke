from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        """
        which model the form reffers to and which fields
        from the model will be render
        """
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """

        super().__init__(*args, **kwargs)
        # here is the placeholders will view in inputs
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_street_address': 'Street Address',
            'default_postcode': 'Postal Code',
            'default_state': 'City',
        }

        # sets autofocus on full name field
        self.fields['default_phone_number'].widget.attrs['autofocus'] = True

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]}'

            # sets attributes for place holder and class and removes labels
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = (
                'border-black rounded-0 profile-form-input'
                )
            self.fields[field].label = False
