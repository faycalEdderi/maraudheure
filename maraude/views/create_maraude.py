from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect

from users.models import *
from maraude.models import *
from maraude.form import *



def create_maraude(request):

    if request.method == 'POST':
        form = CreateMaraudeForm(request.POST)
        
        print("Request : ", request.POST)
        if form.is_valid():

            date = request.POST['date']
            description =  request.POST['description']
            
            get_arrond = request.POST['arrondissement']

            arrondissement = Arrondissement.objects.get(id=get_arrond)

            user = request.user
            association = Association.objects.get(id=user.id)
            
            Maraude.objects.create(
                date = date,
                description = description,
                association = association,
                arrondissement = arrondissement
            )
            return redirect('home')
        else:
            messages.error(request, "Error")
            print(form.errors)
            return redirect('create_maraude')

    else:
        form = CreateMaraudeForm()
        
        args = {
            'form': form,
        }

        return render(request, 'create_maraude.html', args)