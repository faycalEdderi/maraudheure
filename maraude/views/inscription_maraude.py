from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect

from users.models import *
from maraude.models import *
from maraude.form import *

def inscription_maraude(request, pk=None):
    user = request.user
    benevole = Benevole.objects.get(id=user.id)
    maraude = Maraude.objects.get(id=pk)

    maraude.benevole.add(benevole)
    maraude.save()
  
   

    return redirect('home')
    


