from django.core.management import BaseCommand
from core.models import *
import csv

class Command(BaseCommand):
  def handle(self, *args, **options):
    with open('./preguntas.csv', 'r') as archivo:
      # for fila in DictReader(archivo):
      filas = csv.reader(archivo)
      encabezados = next(filas)
      encabezados = ''.join(encabezados).split(';')
      for n_fila, fila in enumerate(filas, start=1):
        try:
          fila = ''.join(fila).split(';')
          record = dict(zip(encabezados, fila))
          # print(record)
          # print(record)
          preg = QuesModel()
          preg.category = record['categoria']
          preg.question = record['pregunta']
          preg.op1 = record['opcion1']
          preg.op2 = record['opcion2']
          preg.op3 = record['opcion3']
          preg.ans = record['respuesta']
          preg.save()
        except Exception:
          print(f'Fila {n_fila}: No pude interpretar: {record}')
