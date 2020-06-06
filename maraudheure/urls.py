from django.contrib import admin
from django.urls import path
from users import views as users_views
from maraude import views as maraude_views


from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', users_views.home, name='home'),
    path("deconnexion/", LogoutView.as_view(), name="logout"),
    path('connexion', users_views.connexion, name='connexion'),

    #URL app users
    path('profil/benevole', users_views.benevole_profil, name="benevole_profil"),
    path('profil/association', users_views.association_profil, name="association_profil"),
    path('profil/modification/benevole', users_views.edit_benevole, name='edit_benevole'),
    path('profil/modification/association', users_views.edit_association, name='edit_association'),
    path('inscription/benevole', users_views.create_benevole, name='create_benevole'),
    path('inscription/association', users_views.create_association, name='inscription_association'),

    # URL app maraude
    path('creation/maraude', maraude_views.create_maraude, name='create_maraude'),
  

]
