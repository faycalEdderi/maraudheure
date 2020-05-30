from django import forms
from django.contrib.auth.models import User
from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm



class CreateBenevoleForm(forms.ModelForm):
    email = forms.EmailField(
        label='Email :',
        required=True,
        error_messages={'required': 'Veuillez entrer une Adresse Mail'},

    )
    username = forms.CharField(
        required=False,
    )
    first_name = forms.CharField(
        label='Prénom : ',
        required=True,
        error_messages={'required': 'Veuillez entrer un prénom'},

    )
    last_name = forms.CharField(
        label='Nom : ',
        required=True,
        error_messages={'required': 'Veuillez entrer un nom'},

    )
    password1 = forms.CharField(
        label="Mot de passe",
        required=False,
        error_messages={'required': 'Les deux mots de passes ne sont pas identiques'},
        widget=forms.PasswordInput,

    )
    password2 = forms.CharField(
        label="Saisir à nouveau le mot de passe",
        required=False,
        error_messages={'required': 'Les deux mots de passes ne sont pas identiques'},
        widget=forms.PasswordInput,
    )
    phone_number = forms.CharField(
        label="Téléphone",
        required=False,  
           
    )
    ville = forms.CharField(
        label="Ville",
        required=False,  
           
    )
    adresse = forms.CharField(
        label="Adresse",
        required=False,  
           
    )

    class Meta:
        model = Benevole
        fields = (
            'email',
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2',
            'phone_number',
            'ville',
            'adresse'
        )


class CreateAssociationForm(forms.ModelForm):
    email = forms.EmailField(
        label='Email :',
        required=True,
        error_messages={'required': 'Veuillez entrer une Adresse Mail'},

    )
    username = forms.CharField(
        required=False,
    )
    first_name = forms.CharField(
        label='Prénom du dirigeant : ',
        required=True,
        error_messages={'required': 'Veuillez entrer un prénom'},

    )
    last_name = forms.CharField(
        label='Nom du dirigeant : ',
        required=True,
        error_messages={'required': 'Veuillez entrer un nom'},

    )
    password1 = forms.CharField(
        label="Mot de passe",
        required=False,
        error_messages={'required': 'Les deux mots de passes ne sont pas identiques'},
        widget=forms.PasswordInput,

    )
    password2 = forms.CharField(
        label="Saisir à nouveau le mot de passe",
        required=False,
        error_messages={'required': 'Les deux mots de passes ne sont pas identiques'},
        widget=forms.PasswordInput,
    )
    phone_number = forms.CharField(
        label="Téléphone",
        required=False,  
           
    )
    num_rna = forms.CharField(
        label="Numéro RNA",
        required=True,  
           
    )
    nom_association = forms.CharField(
        label="Nom de l'association",
        required=True,  
           
    )
    siege_social = forms.CharField(
        label="Adresse du siege social",
        required=True,  
           
    )
    date_creation = forms.CharField(
        label="Date de création de l'association",
        required=True,  
           
    )
    class Meta:
        model = Association
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'phone_number',
            'num_rna',
            'nom_association',
            'siege_social',
            'date_creation',
            
            )

