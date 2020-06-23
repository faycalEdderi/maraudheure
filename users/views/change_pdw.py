from django.shortcuts import render

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import  PasswordChangeForm

from users.models import *
from users.form import *

# Fonction de modification de mot de passe a partir du profile User.
def change_pwd(request):
    
    try:
        connected_user = request.user
        user = User.objects.get(id = connected_user.id)
       
    
        if request.method == 'POST':
            form = PasswordChangeForm(data=request.POST, user=request.user)
            print("Request : ", request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)

                adresse_mail = request.user.email
                '''
                # envoie email lorsque le mot de passe est modifié
                send_mail(
                    'Votre mot de passe à été modifié',
                    'Le changement de mot de passe a été effectué avec succès',
                    'Admin@expleogroup.com',
                    [adresse_mail],
                    fail_silently=False,
                )
                '''
                if user.benevole:
                    return redirect('benevole_profil')
                    
                if user.association:
                    return redirect('association_profil')
            else:
                return redirect('modifMdp')
        else:
            form = PasswordChangeForm(user=request.user)
            args = {'form' : form}

            return render(request, 'change_password.html', args)
    except:
        return redirect('home')


