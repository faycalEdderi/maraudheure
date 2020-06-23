from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from users.models import *
from users.form import *


def edit_benevole(request):
    if request.method == "POST":

        form_edit_profil = EditBenevoleForm(request.POST, request.FILES  or None,
                                        instance=request.user.benevole)
        print("Request : ", request.POST)
        if form_edit_profil.is_valid():

            form_edit_profil.save()

            return redirect("benevole_profil")
        else:
            messages.error(request, "Erreur dans le formulaire")
            return redirect('edit_benevole')
    else:
        form_edit_profil = EditBenevoleForm(instance=request.user.benevole)
        args = { 'form_edit_benevole' : form_edit_profil }

    return render(request, 'edit_profil_benevole.html', args )




def edit_association(request):
    if request.method == "POST":

        form_edit_profil = EditAssociationForm(request.POST, request.FILES  or None,
                                        instance=request.user.association)
        print("Request : ", request.POST)
        if form_edit_profil.is_valid():

            form_edit_profil.save()

            return redirect("association_profil")
        else:
            messages.error(request, "Erreur dans le formulaire")
            return redirect('edit_association')
    else:
        form_edit_profil = EditAssociationForm(instance=request.user.association)
        args = { 'form_edit_association' : form_edit_profil }

    return render(request, 'edit_profil_association.html', args )


def delete_user(request, pk=None):
    
    try:
        connected_user = request.user
        user = User.objects.get(id = connected_user.id)
       
        if user:
            user.delete()
            messages.add_message(request, messages.INFO, 'Votre compte a été supprimé')
            return redirect('home')
        else:
            messages.error(request, "Une erreur s'est produite : votre compte n'a pas été supprimé")
            if user.benevole:
                return redirect('benevole_profil', pk=user.benevole.id)
            if user.association:
                return redirect('association_profil', pk=user.association.id)
    except:
        return redirect('home')


def confirm_delete_account(request):
    try:
        connected_user = request.user
        user = User.objects.get(id = connected_user.id)
        if user:
            return render(request, 'valide_delete_account.html')
    except:
        return redirect('home')

