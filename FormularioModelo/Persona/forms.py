from django import forms
from .models import Persona, Documento

class DocumentoForms(forms.ModelForm):
    class Meta: 
        model = Documento
        fields = ("tipo",)
        widgets = {
            'tipo': forms.TextInput(attrs={'type':'text'})
        }

class PersonaForms(forms.ModelForm):

    class Meta:
        model = Persona
        fields = ("nombre", "apellido", "correo", "tipo_documento")
        widgets = {
            "nombre": forms.TextInput(attrs={'type': 'text','class': 'forms__control'}),
            "apellido": forms.TextInput(attrs={'type': 'text','class': 'forms__control'}),
            "correo": forms.EmailInput(attrs={'type': 'email','class': 'form__control'}),
            'tipo_documento': forms.Select(attrs={'class': 'form__control'})
        }