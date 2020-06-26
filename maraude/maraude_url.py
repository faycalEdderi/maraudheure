from django.contrib import admin
from django.urls import path
from maraude import views as maraude_views


from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
  
    # URL app maraude
    path('/mes_inscrits/<int:pk>/', maraude_views.my_inscriptions, name='my_inscrits'),
    path('/mes_maraudes/<int:pk>/', maraude_views.my_maraudes, name='my_maraudes'),
    path('/benevole/mes_maraudes/<int:pk>/', maraude_views.benevole_maraudes, name='benevole_maraudes'),
    path('/creation/maraude', maraude_views.create_maraude, name='create_maraude'),
    path('/edit/maraude/<int:pk>', maraude_views.edit_maraude, name='edit_maraude'),

    path('/afficher/maraudes', maraude_views.maraude_list, name='maraude_list'),
    path('/afficher/maraude/<int:pk>/', maraude_views.maraude_detail, name='maraude_detail'),
    path('/inscription/maraude/<int:pk>/', maraude_views.inscription_maraude, name='inscription_maraude'),
    path('/desinscription/maraude/<int:pk>/', maraude_views.desinscription_maraude, name='desinscription_maraude'),
    path('/maraude/<int:pk>/delete', maraude_views.delete_maraude, name='delete_maraude'),
  

]
