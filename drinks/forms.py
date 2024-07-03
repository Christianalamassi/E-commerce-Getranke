from django import forms
from .models import Drink, Alcohol


class DrinkForm(forms.ModelForm):
    class Meta:
        model = Drink
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            drinks = Drink.objects.all()
            names = [(c.id, c.get_name()) for c in drinks]

            self.fields['drink'].choices = names
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'border-black'