from django.db import models
from django.contrib.auth.models import User
import django
import random


def upload_location(instance, filename):
    filebase, extension = filename.split(".")
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    filebase = ''.join((random.choice(chars)) for x in range(20))

    return "%s/%s.%s" % (instance.id, filebase, extension)


class Role(models.Model):
    role_name = models.CharField(
        max_length=150,
        unique=True
    )

    def __str__(self):
        return self.role_name


class Benevole(User):

    role = models.ForeignKey(Role, null=True, on_delete=models.CASCADE)

    

    image = models.ImageField(
        upload_to=upload_location,
        null=True,
        blank=True,
    )

    phone_number = models.CharField(
        max_length= 10,
        blank=True, 
        null=True
    )
    activite = models.CharField(
        max_length= 255,
        blank=True, 
        null=True
    )
    metier = models.CharField(
        max_length= 255,
        blank=True, 
        null=True
    )
    hobbies = models.CharField(
        max_length= 255,
        blank=True, 
        null=True
    )
    description = models.CharField(
        max_length= 1500,
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

    image = models.ImageField(
        upload_to=upload_location,
        null=True,
        blank=True,
    )

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

    activite = models.CharField(
        max_length= 1500,
        blank=True, 
        null=True

    )

    description = models.CharField(
        max_length= 5000,
        blank=True, 
        null=True
    )
    
    date_creation = models.DateField(
        blank=True, 
        null=True
    )
    
    phone_number = models.CharField(
        max_length= 10, 
        blank=True, 
        null=True
    )




    def __str__(self):
        return self.nom_association

    class Meta:
        verbose_name = 'Association'
    