from django.db import models
from django.contrib.auth.models import User
import django

class Role(models.Model):
    role_name = models.CharField(
        max_length=150,
        unique=True
    )

    def __str__(self):
        return self.role_name


class Benevole(User):

    role = models.ForeignKey(Role, null=True, on_delete=models.CASCADE)

    phone_number = models.CharField(
        max_length= 10,
        blank=True, 
        null=True
    )
    
    ville = models.CharField(
        max_length= 200, 
        blank=True, 
        null=True 
    )
    adresse = models.CharField(
        max_length= 300,
        blank=True, 
        null=True
    )

    def __str__(self):
        return self.last_name  + " " +  self.first_name

    class Meta:
        verbose_name = 'Bénévole'

    


class Association(User):

    role = models.ForeignKey(Role, null=True, on_delete=models.CASCADE)

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
    
    date_creation = models.DateField()
    
    phone_number = models.CharField(
       max_length= 10, 
       null= True
    )




    def __str__(self):
        return self.nom_association

    class Meta:
        verbose_name = 'Association'
    