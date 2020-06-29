import django_filters
from .models import *

class OsobaFilter(django_filters.FilterSet):

    class Meta:
        model = Osoba
        fields = {
            'imie': ['icontains'],
            'nazwisko': ['icontains']
        }

class TelefonFilter(django_filters.FilterSet):

    class Meta:
        model = Telefon
        fields = {
            'telefon': ['icontains']
        }

class EmailFilter(django_filters.FilterSet):

    class Meta:
        model = Email
        fields = {
            'email': ['icontains']
        }
