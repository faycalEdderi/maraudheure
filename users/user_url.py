from django.contrib import admin
from django.urls import path
from users import views as users_views


from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
   
    #URL app users
    path('profil/benevole', users_views.benevole_profil, name="benevole_profil"),
    path('profil/benevole/edit', users_views.edit_benevole, name="edit_benevole"),
    path('profil/association', users_views.association_profil, name="association_profil"),
    path('profil/association/edit', users_views.edit_association, name="edit_association"),
    path('profil/modification/benevole', users_views.edit_benevole, name='edit_benevole'),
    path('profil/modification/association', users_views.edit_association, name='edit_association'),
    path('inscription/benevole', users_views.create_benevole, name='create_benevole'),
    path('inscription/association', users_views.create_association, name='inscription_association'),
    path('association/<int:pk>/profil', users_views.assoc_public_profil, name='assoc_public_profil'),

]
