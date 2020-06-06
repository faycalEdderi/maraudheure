from django import forms
from .models import *
from django.forms import ModelForm


class CreateMaraudeForm(forms.ModelForm):
 
    date = forms.CharField(
    label="Date de la Maraude",
    required=True,  
        
    )
    description = forms.CharField(
        label='Description : ',
        required=False,
        error_messages={'required': 'Veuillez entrer une description'},

    )

    class Meta:
        model = Benevole
        fields = (
            'date',
            'description',
        )
