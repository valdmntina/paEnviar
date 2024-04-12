from django.shortcuts import render
from django.http import HttpResponse
from .forms import PersonaForms
from .models import Persona

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = PersonaForms(request.POST)
        if form.is_valid():
            form.save()
            return render (request, 'index.html', {
            'form': form
            })
        else:
            print("tamal")
    else:
        form = PersonaForms
        return render (request, 'index.html', {
        'form': form
        })