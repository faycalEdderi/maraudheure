from django.db import models
from django.contrib.auth.models import User
import django

class Benevole(User):

    phone_number = models.CharField(
        max_length= 10
    )

    def __str__(self):
        return self.last_name  + " " +  self.first_name

    class Meta:
        verbose_name = 'Bénévole'

    


class Association(User):

    num_rna = models.CharField(
        max_length= 50,
        null= True
    )

    nom_association = models.CharField(
        max_length= 200,
        null= True
   
    )

    siege_social = models.CharField(
        max_length= 1500,
        null= True

    )
    
    date_creation = models.DateTimeField()
    
    phone_number = models.CharField(
       max_length= 10, 
       null= True
    )




    def __str__(self):
        return self.nom_association

    class Meta:
        verbose_name = 'Association'
    