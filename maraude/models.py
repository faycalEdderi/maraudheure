from users.models import *
from django.db import models
import django


class Maraude(models.Model):
    date = models.DateField(verbose_name = 'Date de maraude')
    description = models.CharField(
        max_length= 2000, 
        blank=True, 
        null=True
    )
    association =  models.ForeignKey(Association,default = "",on_delete=models.CASCADE,blank=True,
                                  null=True)
    
    benevole = models.ManyToManyField(Benevole,blank=True,null=True)
   

    def __str__(self):
        return str(self.date ) + " " + str(self.association)

