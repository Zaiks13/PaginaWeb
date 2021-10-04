from proyecto_register.forms import CsvForm
from django.shortcuts import render
from .forms import CsvForm

# Create your views here.

def csv_list(request):
    return render(request, "proyecto_register/csv_list.html")

def csv_form(request):
    form = CsvForm()
    return render(request, "proyecto_register/csv_form.html", {'form':form})

def csv_delete(request):
    return