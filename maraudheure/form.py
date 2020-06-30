from django import forms





class ContactForm(forms.Form):
    email = forms.EmailField(
        label='Adresse mail :',
        required=True,
        error_messages={'required': 'Veuillez entrer une Adresse Mail'},

    )
    prenom = forms.CharField(
        label='Prenom :',
        required=True,
        error_messages={'required': 'Veuillez entrer une Adresse Mail'},

    )
    message = forms.CharField(
    label="Message",
    required=True,
    widget=forms.Textarea 
        
    )