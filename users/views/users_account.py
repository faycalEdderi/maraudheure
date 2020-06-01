from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from users.models import *
from users.form import *

# Fonction d'affichage du profil benevole
def benevole_profil(request):
    return render(request, "benevole_profil.html")

def association_profil(request):
    return render(request, "association_profil.html")

