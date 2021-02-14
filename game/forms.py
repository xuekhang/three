from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Config

class ConfigForm(forms.ModelForm):
    # letter = forms.MultipleChoiceField(choices= LETTERS)
    def __init__(self, *args, **kwargs):
        super(ConfigForm, self).__init__(*args, **kwargs)
        self.fields['game_code'].widget.attrs['disabled'] = True
    class Meta:
        model = Config
        fields = ['num_of_players','num_of_rounds','letters','game_code']
        # widgets   = {
        #     'game_code' : forms.Textarea(attrs={'cols': 80, 'rows': 20}),

        # }

