from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from users import models
import random


def inicio(request):
  template = "index.html"
  contexto = {}
  return render(request, template, contexto)

@login_required
def compartir(request):
  return render(request, "share.html")


@login_required
def ranking(request):
  form = models.Perfil.objects.filter(is_staff=False).order_by('-puntaje').values('username', 'puntaje')[:10]
  context = {
    'form': form
  }
  return render(request, "ranking.html", context)


@login_required
def resultado(request):
  if request.method != "POST":
    return redirect('inicio')
  else:
    return render(request, "resultado.html")


@login_required
def jugar(request):
  '''
    crea contador de preguntas
    crea acumulador de puntaje
    pregunta al azar
    obtiene pregunta y despliega en pantalla categoría y opciones
    valida opción correcta
    acumula puntaje
  '''
  
  if request.POST.get("numeroPregunta"):
    numeroPregunta = int(request.POST.get("numeroPregunta"))
    score = int(request.POST.get("score"))
    correct = int(request.POST.get("correct"))
    wrong = int(request.POST.get("wrong"))
    ids = list(request.POST.get("ids"))
  else:
    numeroPregunta = 1 
    score = 0
    wrong = 0
    correct = 0
    ids = []

  if request.method != "POST":
    electorDeCategoria = random.choice(range(QuesModel.objects.all().count()))
    while str(electorDeCategoria) in ids:
      electorDeCategoria = random.choice(range(QuesModel.objects.all().count()))
    ids.append(electorDeCategoria)
    form = QuesModel.objects.get(pk=electorDeCategoria)
    context = {
      'form':form,
      "numeroPregunta":numeroPregunta,
      'score':score,
      'correct':correct,
      'wrong':wrong,
      'ids': ids
    }
    return render(request, "play.html", context)
  elif  request.method == 'POST':
    if numeroPregunta < 5:
      questions = QuesModel.objects.get(pk=int(request.POST.get("ID")))
      opcionSeleccionada=request.POST.get("opcionMarcada")
      if request.POST.get(opcionSeleccionada) == questions.ans:
        # score = int(request.POST.get("score"))
        score += int(request.POST.get("timer")) * 10
        # correct = int(request.POST.get("correct")) + 1
        correct += 1
        print('puntaje:', score, 'corectas:', correct, 'Nro Pregunta:', numeroPregunta)
      else:
        # wrong = int(request.POST.get("wrong")) + 1
        wrong += 1
        print('incorrectas:', wrong, 'Nro Pregunta:', numeroPregunta)
      numeroPregunta += 1 # próxima pregunta
      electorDeCategoria = random.choice(range(QuesModel.objects.all().count()))
      while str(electorDeCategoria) in ids:
        electorDeCategoria = random.choice(range(QuesModel.objects.all().count()))
      ids.append(electorDeCategoria)
      questions = QuesModel.objects.get(pk=electorDeCategoria)
      context = {
        'score':score,
        'correct':correct,
        'wrong':wrong,
        'numeroPregunta':numeroPregunta,
        'form':questions,
        'ids': ids
      }
      return render(request,'play.html',context)
    else:
      questions = QuesModel.objects.get(pk=int(request.POST.get("ID")))
      opcionSeleccionada = request.POST.get("opcionMarcada")
      if request.POST.get(opcionSeleccionada) == questions.ans:
        # score = int(request.POST.get("score")) + 10
        score += int(request.POST.get("timer")) * score
        # correct = int(request.POST.get("correct")) + 1
        correct += 1
        print('puntaje:', score, 'corectas:', correct, 'Nro Pregunta:', numeroPregunta)
      else:
        # wrong = int(request.POST.get("wrong")) + 1
        wrong += 1
        print('incorrectas:', wrong, 'Nro Pregunta:', numeroPregunta)
      
      user = request.user
      if user.puntaje is None or user.puntaje < score:
        user.puntaje = score
        user.save()
      context = {
        'score': score,
        'correct': correct,
        'wrong': wrong,
        'numeroPregunta': numeroPregunta,
        'ids': ids
      }
      return render(request,'resultado.html',context)
