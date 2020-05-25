from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect

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

