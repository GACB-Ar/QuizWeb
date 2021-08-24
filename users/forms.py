from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.db import models
from django.db.models import fields
from .models import Perfil


class NuevoPerfilForm(UserCreationForm):
  class Meta:
    model = Perfil
    fields = (
      "first_name",
      "last_name",
      "username",
      "email",
      "password1",
      "password2",
    )


class EditarPerfilForm(UserChangeForm):
  class Meta:
    model = Perfil
    fields = (
      "first_name",
      "last_name",
      "username",
      "email",
    )


class CambiarPassword(PasswordChangeForm):
  class Meta:
    model = Perfil
    fields = (
      "old_password",
      "new_password1",
      "new_password2",
    )
