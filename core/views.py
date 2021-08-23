from django.http import request
from django.shortcuts import render
import random

# Create your views here.

# def inicio(request):
#   return render(request, 'index.html')


def inicio(request):
  # if request.user.is_authenticated: #and request.user.is_staff:
  #   template = "admin_dashboard.html"
  # else:
  template = "index.html"
  contexto = {}
  return render(request, template, contexto)


def jugar(request):
  '''
    crear contador de preguntas
    crear acumulador de puntaje
    Elegir pregunta al azar
    obtener respuestas y desplegar en pantalla categoría y respuestas
    validar correcta en valor de respuesta
    acumular puntaje
  '''
  return render(request, 'play.html')
