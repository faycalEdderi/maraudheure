from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect

from users.models import *
from maraude.models import *
from maraude.form import *

def maraude_list(request):
    maraudes = Maraude.objects.all()

    context = {
        'maraudes': maraudes,
    }
    return render(request, "maraude_list.html", context)
    

def maraude_detail(request, pk=None):
    select_maraude = Maraude.objects.get(id=pk)
    
    context = {
        "maraude": select_maraude,
    }

    return render(request, 'maraude_detail.html', context)

