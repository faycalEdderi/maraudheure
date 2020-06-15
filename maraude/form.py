from django import forms
from .models import *
from django.forms import ModelForm

class DateInput(forms.DateInput):
    input_type="date"

class CreateMaraudeForm(forms.ModelForm):
 
   
    date = forms.DateField(
        label="Date de la Maraude",
        widget= DateInput
    )
    description = forms.CharField(
        label='Description : ',
        required=False,
        error_messages={'required': 'Veuillez entrer une description'},

    )
    arrondissement = forms.ModelChoiceField(
        label="Arrondissement : ",
        required=True,
        queryset= Arrondissement.objects.all()
    )

    class Meta:
        model = Association
        fields = (
            'date',
            'description',
            'arrondissement'
        )
