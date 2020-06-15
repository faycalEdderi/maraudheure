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
    heure_debut = forms.CharField(
        label='Heure de debut : ',
        required=False,
        error_messages={'required': 'Veuillez entrer une heure de debut'},

    )
    heure_fin = forms.CharField(
        label='Heure de fin : ',
        required=False,
        error_messages={'required': 'Veuillez entrer une heure de fin'},

    )
    adresse = forms.CharField(
        label='Adresse : ',
        required=False,
        error_messages={'required': 'Veuillez entrer une adresse'},

    )

    arrondissement = forms.ModelChoiceField(
        label="Arrondissement : ",
        required=True,
        queryset= Arrondissement.objects.all()
    )
    

    products = Product.objects.all()
    produits = forms.ModelMultipleChoiceField(
        label="Type de distribution ",
        widget=forms.CheckboxSelectMultiple, required=True, 
        queryset=products)

    class Meta:
        model = Maraude
        fields = (
            'date',
            'description',
            'heure_debut',
            'heure_fin',
            'adresse',
            'arrondissement',
            'produits'
        )
