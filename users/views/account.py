from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect

from users.models import *
from users.form import *

def home(request):
    return render(request,'home.html')

def connexion(request):

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                print("user connected : ", user.email)
                return redirect('home')

        else:
            messages.error(request,'Adresse mail ou mot de passe incorrect') 
            print("user not connected")
            return redirect('connexion')

        return render(request,'uos_list.html')
    else:
        form = AuthenticationForm()
    return render(request, 'connexion.html', {'form': form})

    # Fonction de création utilisateur
def create_benevole(request):

    if request.method == 'POST':
        form = CreateBenevoleForm(request.POST)


        print("Request : ", request.POST)
        if form.is_valid():

            email = request.POST['email']
           
            nom = request.POST['last_name']
            prenom = request.POST['first_name']
            mdp1 = request.POST['password1']
            mdp2 = request.POST['password2']

            print("request : ", request.POST)
            '''
            send_mail(
                'Votre compte a été créé',
                'Votre mdp : ' + mdp,
                'Admin@expleogroup.com',
                [email],
                fail_silently=False,
            )
            '''
            return redirect('connexion')
        else:
            messages.error(request, "Error")
            return redirect('create_benevole')

    else:
        form = CreateBenevoleForm()


        args = {
            'form': form,


        }

        return render(request, 'create_benevole.html', args)




