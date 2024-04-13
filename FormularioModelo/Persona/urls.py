from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('documento/', views.documento, name='documento'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
]
