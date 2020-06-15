import django_filters 
from django import forms
from maraude.models import *


class DateInput(forms.DateInput):
    input_type = 'date'

class MaraudeFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(widget=DateInput(attrs={'type': 'date'}))
    class Meta:
        model =  Maraude
        fields=['arrondissement', 'date', 'association']