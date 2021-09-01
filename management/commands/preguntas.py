from django.core.management import BaseCommand
from core.models import *
from csv import DictReader

class Command(BaseCommand):
  def handle(self, *args, **options):
    with open('../preguntas.csv', 'r') as archivo:
      for fila in DictReader(open(archivo)):
        print(fila)
        pregunta = QuesModel()
        pregunta.category = fila['categoria']
        pregunta.question = fila['pregunta']
        pregunta.op1 = fila['opcion1']
        pregunta.op2 = fila['opcion2']
        pregunta.op3 = fila['opcion3']
        pregunta.ans = fila['respuesta']
        pregunta.save()
