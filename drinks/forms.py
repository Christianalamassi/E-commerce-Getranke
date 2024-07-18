from django import forms
from .widgets import CustomClearableFileInput
from .models import Drink, Alcohol


class DrinkForm(forms.ModelForm):
    class Meta:
        model = Drink
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        drinks = Drink.objects.all()
    
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'
            self.fields['name'].label = 'Name of Drink'
