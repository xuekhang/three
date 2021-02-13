from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Config, Car

LETTERS = ('A','B','C')

class ConfigForm(forms.ModelForm):
    # letter = forms.MultipleChoiceField(choices= LETTERS)
    class Meta:
        model = Config
        fields = ['num_of_player']


COLORS= (
    ('R', 'Red'),
    ('Y', 'Yellow'),
    ('W', 'White'),
)

class CarAdminForm(forms.ModelForm):
    color = forms.MultipleChoiceField(choices = COLORS)

    class Meta:
        model = Car
        fields = '__all__'

    def clean_color(self):
        color = self.cleaned_data['color']
        if not color:
            raise forms.ValidationError("...")

        if len(color) > 2:
            raise forms.ValidationError("...")

        color = ''.join(color)
        return color
