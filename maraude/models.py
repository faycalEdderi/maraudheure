from users.models import *
from django.db import models
import django

class Arrondissement(models.Model):
    LIST_ARROND = (
        ('1er Arrondissement', '75101'),
        ('2e Arrondissement', '75102'),
        ('3e Arrondissement', '75103'),
        ('4e Arrondissement', '75104'),
        ('5e Arrondissement', '75105'),
        ('6e Arrondissement', '75106'),
        ('7e Arrondissement', '75107'),
        ('8e Arrondissement', '75108'),
        ('9e Arrondissement', '75109'),
        ('10e Arrondissement', '75110'),
        ('11e Arrondissement', '75111'),
        ('12e Arrondissement', '75112'),
        ('13e Arrondissement', '75113'),
        ('14e Arrondissement', '75114'),
        ('15e Arrondissement', '75115'),
        ('16e Arrondissement', '75116'),
        ('17e Arrondissement', '75117'),
        ('18e Arrondissement', '75118'),
        ('19e Arrondissement', '75119'),
        ('20e Arrondissement', '75120'),
        
        
    )
    n_arrondissement = models.CharField(max_length=300, choices=LIST_ARROND, unique=True )

    def __str__(self):
        return str(self.n_arrondissement )


class Maraude(models.Model):
    date = models.DateField(verbose_name = 'Date de maraude')
    description = models.CharField(
        max_length= 2000, 
        blank=True, 
        null=True
    )
    association =  models.ForeignKey(Association,default = "",on_delete=models.CASCADE,blank=True,
                                  null=True, related_name='my_maraude')


    arrondissement =  models.ForeignKey(Arrondissement,default = "",on_delete=models.CASCADE,blank=True,
                                  null=True)
    
    
    benevole = models.ManyToManyField(Benevole,blank=True, related_name='maraude_benevole')
   

    def __str__(self):
        return str(self.date ) + " " + str(self.association)

