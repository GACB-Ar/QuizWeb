from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Perfil(AbstractUser):
  puntaje = models.IntegerField(null=True)

  def __str__(self) -> str:
    return f'{self.id}: {self.username} {self.first_name} {self.last_name} {self.email} {self.is_staff} {self.is_active} {self.puntaje}'
