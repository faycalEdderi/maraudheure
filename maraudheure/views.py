from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from users.models import *
from users.form import *

# Fonction d'affichage de la page permettant de selectionné le type de profil a creer
def account_type(request):
    return render(request, "bene_ou_asso.html")



