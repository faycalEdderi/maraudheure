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

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        user = super(CreateBenevoleForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user