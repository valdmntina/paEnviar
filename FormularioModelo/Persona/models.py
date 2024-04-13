from django.db import models

# Create your models here.

class Documento(models.Model):
    tipo = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.tipo

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_documento = models.OneToOneField(Documento, max_length=10, on_delete=models.PROTECT,  null=True)
    imagen = models.ImageField(null=True, blank=True)


