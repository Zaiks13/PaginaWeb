from django import forms
from django.forms import fields
from .models import Csv

class CsvForm(forms.ModelForm):

    class Meta:
        model = Csv
        # Para especificar parámetros poner:
        # fields = ('p1', ... ,'pn')
        fields = '__all__'

        labels = {
            'csv' : 'Archivo .csv'
        }