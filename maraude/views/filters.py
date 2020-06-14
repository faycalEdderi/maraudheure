import django_filters 
from maraude.models import *

class MaraudeFilter(django_filters.FilterSet):
    class Meta:
        model =  Maraude
        fields=['arrondissement', 'date', 'association']