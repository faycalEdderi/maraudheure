from django import forms
from django.contrib.auth.models import User
from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

class DateInput(forms.DateInput):
    input_type="date"

class CreateBenevoleForm(forms.ModelForm):
    email = forms.EmailField(
        label='Email :',
        required=True,
        error_messages={'required': 'Veuillez entrer une Adresse Mail'},

    )
    image = forms.ImageField(
        label="Photo de profil :",
        required=False,
        error_messages={ 'invalid': "Veuillez selectionner uniquement un fichier de type "
                                    "image"},
        widget=forms.FileInput,
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
        widget=forms.TextInput(attrs={'class':'form-creation-input'})

    )
    password1 = forms.CharField(
        label="Mot de passe :",
        required=False,
        error_messages={'required': 'Les deux mots de passes ne sont pas identiques'},
        widget=forms.PasswordInput,

    )
    password2 = forms.CharField(
        label="Confirmer :",
        required=False,
        error_messages={'required': 'Les deux mots de passes ne sont pas identiques'},
        widget=forms.PasswordInput,
    )
    phone_number = forms.CharField(
        label="Téléphone :",
        required=False,  
           
    )
    ville = forms.CharField(
        label="Ville :",
        required=False,  
           
    )
    adresse = forms.CharField(
        label="Adresse :",
        required=False,  
           
    )

    class Meta:
        model = Benevole
        fields = (
            'email',
            'image',
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
    
    
    password1 = forms.CharField(
        label="Mot de passe :",
        required=False,
        error_messages={'required': 'Les deux mots de passes ne sont pas identiques'},
        widget=forms.PasswordInput,

    )
    password2 = forms.CharField(
        label="Confirmer :",
        required=False,
        error_messages={'required': 'Les deux mots de passes ne sont pas identiques'},
        widget=forms.PasswordInput,
    )
    
    num_rna = forms.CharField(
        label="Numéro RNA :",
        required=True,  
           
    )
    nom_association = forms.CharField(
        label="Nom de l'association :",
        required=True,  
           
    )
    siege_social = forms.CharField(
        label="Adresse du siege social :",
        required=True,  
           
    )



    
    class Meta:
        model = Association
        fields = (
            'username',
            
            
            'email',
            'password1',
            'password2',
           
            'num_rna',
            'nom_association',
            'siege_social',
            
            
            )

class EditAssociationForm(forms.ModelForm):
    email = forms.EmailField(
        label='Email :',
        required=True,
        error_messages={'required': 'Veuillez entrer une Adresse Mail'},

    )
    image = forms.ImageField(
        label="Photo de profil :",
        required=False,
        error_messages={ 'invalid': "Veuillez selectionner uniquement un fichier de type "
                                    "image"},
        widget=forms.FileInput,
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
   
    phone_number = forms.CharField(
        label="Téléphone",
        required=False,  
           
    )
    nom_association = forms.CharField(
        label="Nom de l'association",
        required=True,  
           
    )
    siege_social = forms.CharField(
        label="Adresse du siege social",
        required=True,  
           
    )

    activite = forms.CharField(
        label="Activité de l'association",
        required=True,  
           
    )

    description = forms.CharField(
        label="Description de l'association",
        required=True,  
        widget=forms.Textarea 
         
    )

    
    class Meta:
        model = Association
        fields = (
           
            'first_name',
            'last_name',
            'email',
            'image',
            'nom_association',
            'phone_number',
            'siege_social',
            'activite',  
            'description',          
            )

class EditBenevoleForm(forms.ModelForm):
    email = forms.EmailField(
        label='Email :',
        required=True,
        error_messages={'required': 'Veuillez entrer une Adresse Mail'},

    )
    image = forms.ImageField(
        label="Photo de profil :",
        required=False,
        error_messages={ 'invalid': "Veuillez selectionner uniquement un fichier de type "
                                    "image"},
        widget=forms.FileInput,
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
    activite = forms.CharField(
        label="Activité",
        required=False,  
           
    )
    hobbies = forms.CharField(
        label="Hobbies",
        required=False,  
           
    )
    metier = forms.CharField(
        label="Metier",
        required=False,  
           
    )
    description = forms.CharField(
        label="Description de l'association",
        required=False,  
        widget=forms.Textarea 
         
    )

    class Meta:
        model = Benevole
        fields = (
            'email',
            'image',
            'first_name',
            'last_name',
            'phone_number',
            'ville',
            'adresse',
            'activite',
            'hobbies',
            'metier',
            'description'
        )


