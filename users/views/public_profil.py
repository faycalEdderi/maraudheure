from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from users.models import *
from users.form import *


# Fonction d'affichage du profil public d'une association
def assoc_public_profil(request, pk=None):
  
    association = Association.objects.get(id=pk)

    if association:
    
        context = {
            "association": association,
        }
    return render(request, 'assoc_public_profil.html', context)


    



