from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from users.models import *
from users.form import *

def home(request):
    return render(request,'home.html')



def connexion(request):

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                print("user connected : ", user.email)
                return redirect('home')

        else:
            messages.error(request,'Adresse mail ou mot de passe incorrect') 
            print("erro : ", form.errors)
            print("user not connected")
            return redirect('connexion')

        return render(request,'uos_list.html')
    else:
        form = AuthenticationForm()
    return render(request, 'connexion.html', {'form': form})

    # Fonction de création utilisateur
def create_benevole(request):

    if request.method == 'POST':
        form = CreateBenevoleForm(request.POST, request.FILES)


        print("Request : ", request.POST)
        if form.is_valid():

            email = request.POST['email']
          
            nom = request.POST['last_name']
            prenom = request.POST['first_name']
            image = request.FILES['image']
            mdp1 = request.POST['password1']
            mdp2 = request.POST['password2']

            select_role = Role.objects.get(role_name = "benevole" )
            get_role = Role.objects.get(id = select_role.id )
            
            new_benevole = Benevole(
                username = nom + '_' + prenom,  
                email = email, 
                first_name = prenom,
                last_name = nom,
                image= image,
                role=get_role
            )
         
            if mdp1 == mdp2:

                new_benevole.set_password(mdp1)
        
                new_benevole.save()
                print("user created")
            else:
                messages.error(request, "Les mots de passes ne sont pas identiques")
                return redirect('inscription_benevole')
            '''
            send_mail(
                'Votre compte a été créé',
                'Votre mdp : ' + mdp,
                'Admin@expleogroup.com',
                [email],
                fail_silently=False,
            )
            '''
            return redirect('connexion')
        else:
            messages.error(request, "Error")
            return redirect('create_benevole')

    else:
        form = CreateBenevoleForm()
        args = {
            'form': form,
        }

        return render(request, 'create_benevole.html', args)


def create_association(request):

    if request.method == 'POST':
        form = CreateAssociationForm(request.POST, request.FILES)

        print("Request : ", request.POST)
        if form.is_valid():

            email = request.POST['email']
          
            nom = request.POST['last_name']
            prenom = request.POST['first_name']
            mdp1 = request.POST['password1']
            mdp2 = request.POST['password2']

            image = request.FILES['image']

            num_rna = request.POST['num_rna']
            nom_association = request.POST['nom_association']
            siege = request.POST['siege_social']
            date = request.POST['date_creation']
            telephone = request.POST['phone_number']

            description = request.POST['description']
            activite = request.POST['activite']


            select_role = Role.objects.get(role_name = "association" )
            get_role = Role.objects.get(id = select_role.id )

            
            
            new_association = Association(
                username = nom + '_' + prenom,  
                email = email, 
                image=image,
                first_name = prenom,
                last_name = nom,
                role=get_role,
                num_rna = num_rna,
                nom_association = nom_association,
                siege_social = siege,
                date_creation = date,
                phone_number = telephone,
                activite = activite,
                description = description
            )
         
            if mdp1 == mdp2:

                new_association.set_password(mdp1)
        
                new_association.save()
                print("association created")
            else:
                messages.error(request, "Les mots de passes ne sont pas identiques")
                return redirect('inscription_association')
            '''
            send_mail(
                'Votre compte a été créé',
                'Votre mdp : ' + mdp,
                'Admin@expleogroup.com',
                [email],
                fail_silently=False,
            )
            '''
            return redirect('connexion')
        else:
            messages.error(request, form.errors)
         
            return redirect('inscription_association')

    else:
        form = CreateAssociationForm()


        args = {
            'form': form,
        }

        return render(request, 'create_association.html', args)








