from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
import random


def inicio(request):
  # if request.user.is_authenticated: #and request.user.is_staff:
  #   template = "admin_dashboard.html"
  # else:
  template = "index.html"
  contexto = {}
  return render(request, template, contexto)

@login_required
def compartir(request):
  return render(request, "share.html")

def index2(request):
  # if request.user.is_authenticated: #and request.user.is_staff:
  #   template = "admin_dashboard.html"
  # else:
  template = "index2.html"
  contexto = {}
  return render(request, template, contexto)


@login_required
def jugar(request):
  '''
    crear contador de preguntas
    crear acumulador de puntaje
    Elegir pregunta al azar
    obtener respuestas y desplegar en pantalla categoría y respuestas
    validar correcta en valor de respuesta
    acumular puntaje
  '''
  
  if request.POST.get("numeroPregunta"):
    numeroPregunta=int(request.POST.get("numeroPregunta"))
    score= int(request.POST.get("score"))     
    correct=int(request.POST.get("correct"))
    wrong=int(request.POST.get("wrong"))
  else:
    numeroPregunta=1 
    score=0
    wrong=0
    correct=0

  if request.method!= "POST":
    electorDeCategoria= random.choice(range(26))
    form = QuesModel.objects.get(pk=electorDeCategoria)
    context = {
      'form':form,
      "numeroPregunta":numeroPregunta,
      'score':score,
      'correct':correct,
      'wrong':wrong,
    }
    return render(request, "play.html", context)
  elif  request.method == 'POST':
    if numeroPregunta<5:
      questions = QuesModel.objects.get(pk=int(request.POST.get("ID")))
      opcionSeleccionada=request.POST.get("opcionMarcada")
      if request.POST.get(opcionSeleccionada) == questions.ans:
        score= int(request.POST.get("score"))+10
        correct=int(request.POST.get("correct"))+1
        print('puntaje:', score, 'corectas:', correct, 'Nro Pregunta:', numeroPregunta)
      else:
        wrong=int(request.POST.get("wrong"))+1
        print('incorrectas:', wrong, 'Nro Pregunta:', numeroPregunta)
      numeroPregunta+=1 # próxima pregunta
      electorDeCategoria= random.choice(range(26))
      questions = QuesModel.objects.get(pk=electorDeCategoria)
      context = {
        'score':score,
        'correct':correct,
        'wrong':wrong,
        "numeroPregunta":numeroPregunta,
        'form':questions
      }
      return render(request,'play.html',context)
    else:
      questions = QuesModel.objects.get(pk=int(request.POST.get("ID")))
      opcionSeleccionada = request.POST.get("opcionMarcada")
      if request.POST.get(opcionSeleccionada) == questions.ans:
        score = int(request.POST.get("score"))+10
        correct = int(request.POST.get("correct"))+1
        print('puntaje:', score, 'corectas:', correct, 'Nro Pregunta:', numeroPregunta)
      else:
        wrong = int(request.POST.get("wrong"))+1
        print('incorrectas:', wrong, 'Nro Pregunta:', numeroPregunta)
      # return render(request,'index2.html')
      #cambiar y poner que mande a la pagina de los resultados
      return redirect("index2")  # la de resultado todavia no tenemos








 
    
  
  

  
  
