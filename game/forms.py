from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Config

class ConfigForm(forms.ModelForm):
    # letter = forms.MultipleChoiceField(choices= LETTERS)
    class Meta:
        model = Config
        fields = ['num_of_players','num_of_rounds','letters']

