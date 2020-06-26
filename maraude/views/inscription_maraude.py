from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect

from users.models import *
from maraude.models import *
from maraude.form import *


# fonction d'inscription a une maraude pour un bénévole
def inscription_maraude(request, pk=None):
    user = request.user
    benevole = Benevole.objects.get(id=user.id)
    maraude = Maraude.objects.get(id=pk)

    maraude.benevole.add(benevole)
    maraude.save()
  
    return redirect('home')
    
# fonction d'inscription a une maraude pour un bénévole
def desinscription_maraude(request, pk=None):
    try:

        user = request.user
        benevole = Benevole.objects.get(id=user.id)
        maraude = Maraude.objects.get(id=pk)
        if user:

            maraude.benevole.remove(benevole)
        
            maraude.save()
            messages.add_message(request, messages.INFO, 'Vous etes désinscrit de la maraude')
            return redirect('home')
        else:
            messages.error(request, "Une erreur s'est produite : votre compte n'a pas été supprimé")
    
            return redirect('desinscription_maraude')
    except:
        messages.error(request, "Une erreur s'est produite : Vous n'etes pas autorisé à acceder à cette page")
        return redirect('home')
    





