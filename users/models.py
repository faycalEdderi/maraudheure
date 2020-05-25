from django.db import models
from django.contrib.auth.models import User

class MyUsers(User):

    phone_number =  models.CharField(
        max_length=100)



    def __str__(self):
        return self.last_name  + " " +  self.first_name

    class Meta:
        verbose_name = 'MyUser'

class Benevole(User):

    phone_number =  models.CharField(
        max_length=100, 
        null=True,
        blank=True,
        )

    def __str__(self):
        return self.last_name  + " " +  self.first_name

    class Meta:
        verbose_name = 'Bénévole'
