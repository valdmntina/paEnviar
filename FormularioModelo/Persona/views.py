from django.shortcuts import render
from django.http import HttpResponse
from .forms import PersonaForms, DocumentoForms
from .models import Persona, Documento

# Create your views here.

def index(request):
    documento = request.POST.get('documento_identidad')
    if request.method == "POST":
        if request.method == 'POST':
            form = PersonaForms(request.POST, files=request.FILES)
            if form.is_valid():
                form.save()
    else:
        form = PersonaForms
    return render (request, 'index.html', {'form':form})
    
def documento(request):
    if request.method == "POST":
        form = DocumentoForms(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = DocumentoForms()
    return render (request, 'documento.html', {'form':form})

def eliminar(request, id):
    documento = Documento.objects.get(id=id)
    documento.delete()
    return HttpResponse ("se elimino su buebada")