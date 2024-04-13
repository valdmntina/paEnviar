from django.shortcuts import render
from django.http import HttpResponse
from .forms import PersonaForms, DocumentoForms
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
    
def documento(request):
    if request.method == "POST":
        form = DocumentoForms(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = DocumentoForms()
        return render (request, 'documento.html', {
        'form': form
        })