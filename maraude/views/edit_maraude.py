from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect

from users.models import *
from maraude.models import *
from maraude.form import *



def edit_maraude(request, pk=None):
    maraude = Maraude.objects.get(id=pk)
    connected_user = request.user
    if request.method == "POST":

        form_edit_maraude = EditMaraudeForm(request.POST, request.FILES  or None,
                                        instance=maraude)
        print("Request : ", request.POST)
        get_service = request.POST.getlist('produits')
        if form_edit_maraude.is_valid():

            form_edit_maraude.save()
            if get_service:

                maraude.produit.set(get_service)

            return redirect("my_maraudes", pk=connected_user.id)
        else:
            messages.error(request, "Erreur dans le formulaire")
            return redirect('edit_maraude')
    else:
        form_edit_maraude = EditMaraudeForm(instance=maraude)
        args = { 'form' : form_edit_maraude }

    return render(request, 'edit_maraude.html', args )