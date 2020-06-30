from django.shortcuts import render

from django.contrib import messages
from django.shortcuts import render, redirect
from .form import *
from django.core.mail import send_mail





# Fonction d'affichage de la page permettant de selectionné le type de profil a creer
def account_type(request):
    return render(request, "bene_ou_asso.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)


        print("Request : ", request.POST)
        if form.is_valid():

            email = request.POST['email']
        
       
            prenom = request.POST['prenom']
            message = request.POST['message']
        
            
            send_mail(
                prenom + ' : ' + email,
                message,
                email,
                ["fayc.edderi@live.fr"],
                fail_silently=False,
            )
            messages.add_message(request, messages.INFO, 'Votre message a été envoyé')
            
            return redirect('contact')
        else:
            messages.error(request, "Error")
            return redirect('contact')

    else:
        form = ContactForm()
        args = {
            'form': form,
        }

        return render(request, "contact.html", args)

    


