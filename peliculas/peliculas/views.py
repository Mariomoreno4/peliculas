from django.http import HttpResponse

from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages




class Persona(object):
    
    def __init__(self,nombre,apellido) :
        self.nombre=nombre
        self.apellido=apellido

  


def prin(request):
    return render(request, "Prin.html")
    
       
    