from django.shortcuts import render

from django.template import loader
from django.http import HttpResponse

from .models import flia
# Create your views here.

def crear(request):
    
    familiar1 = flia(nombre = 'Juan', identificacion = 123456789, nacionalidad = 'Colombia', fecha_naci = '2002-11-13')
    familiar1.save()
    
    familiar2 = flia(nombre = 'Daniela', identificacion = 789456, nacionalidad = 'Argentina', fecha_naci = '1971-10-30')
    familiar2.save()
    
    familiar3 = flia(nombre = 'Micaela', identificacion = 123456, nacionalidad = 'Argentina', fecha_naci = '1995-09-11')
    familiar3.save()


    return HttpResponse('Creado con éxtio.')

def mostrar(request):
    
    info = flia.objects.all()
    
    dicc = { 'FAMILIARES' : info }
    
    plantilla = loader.get_template('index.html')
    
    documento = plantilla.render( dicc )
    
    return HttpResponse( documento )