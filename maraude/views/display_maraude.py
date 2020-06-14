from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect

from users.models import *
from maraude.models import *
from maraude.form import *
from .filters import *


# afficher toutes les maraudes 
def maraude_list(request):
    maraudes = Maraude.objects.all()

    myFilter =MaraudeFilter(request.GET, queryset=maraudes)
    maraudes = myFilter.qs

    context = {
        'maraudes': maraudes,
        'myFilter': myFilter
    }
    return render(request, "maraude_list.html", context)
    

# afficher les details d'une maraude
def maraude_detail(request, pk=None):
    select_maraude = Maraude.objects.get(id=pk)
    
    context = {
        "maraude": select_maraude,
    }

    return render(request, 'maraude_detail.html', context)


# afficher les inscrit d'une maraude pour une association
def my_inscriptions(request, pk=None):
    try:
        connected_user = request.user
        association = Association.objects.get(id=connected_user.id)
        if association and connected_user:
            my_maraudes = association.my_maraude.all()

            context = {
                "my_maraudes": my_maraudes,
            }
            return render(request, 'mes_inscrits.html', context)
    except:
        return redirect('connexion')

# pour un association : affiche tous ses maraudes
def my_maraudes(request, pk=None):

    connected_user = request.user
    print("ID :",connected_user.id)
    
    association = Association.objects.get(id=connected_user.id)

    if association and connected_user:
        my_maraudes = association.my_maraude.all()

        context = {
            "my_maraudes": my_maraudes,
        }
    return render(request, 'association_mes_maraudes.html', context)


# pour benevole : affiches les maraude ou je suis inscrit
def benevole_maraudes(request, pk=None):

    connected_user = request.user
    print("ID :",connected_user.id)
    
    benevole = Benevole.objects.get(id=connected_user.id)

    if benevole and connected_user:
        my_maraudes = benevole.maraude_benevole.all()

        context = {
            "my_maraudes": my_maraudes,
        }
    return render(request, 'benevole_maraudes.html', context)


    
