from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, AuthenticationForm
from django import forms
from .models import Perfil


class IniciarSesionForm(AuthenticationForm):
  class Meta:
    model = Perfil
    fields = (
      "username",
      "password"
    )
  
  def __init__(self, *args, **kwargs):
    super(IniciarSesionForm, self).__init__(*args, **kwargs)
    self.fields['username'].widget = forms.TextInput(
        attrs={'class': 'form-input', 'placeholder': 'ingrese su usuario'})
    self.fields['password'].widget = forms.PasswordInput(
        attrs={'class': 'form-input', 'placeholder': 'ingrese su contraseña'})


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

    widgets = {
      'first_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'ingrese su nombre'}),
      'last_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'ingrese su apellido'}),
      'username': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'nombre de usuario'}),
      'email': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'ingrese su email'})
    }

  def __init__(self, *args, **kwargs):
    super(NuevoPerfilForm, self).__init__(*args, **kwargs)
    self.fields['password1'].widget = forms.PasswordInput(
        attrs={'class': 'form-input', 'placeholder': 'ingrese su contraseña'})
    self.fields['password2'].widget = forms.PasswordInput(
        attrs={'class': 'form-input', 'placeholder': 'confirme su contraseña'})


class EditarPerfilForm(UserChangeForm):
  class Meta:
    model = Perfil
    fields = (
      "first_name",
      "last_name",
      "username",
      "email",
    )

    widgets = {
      'first_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'ingrese su nombre'}),
      'last_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'ingrese su apellido'}),
      'username': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'nombre de usuario'}),
      'email': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'ingrese su email'})
    }


class CambiarPassword(PasswordChangeForm):
  class Meta:
    model = Perfil
    fields = (
      "old_password",
      "new_password1",
      "new_password2",
    )

  def __init__(self, *args, **kwargs):
    super(CambiarPassword, self).__init__(*args, **kwargs)
    self.fields['old_password'].widget = forms.PasswordInput(
        attrs={'class': 'form-input', 'placeholder': 'contraseña anterior'})
    self.fields['new_password1'].widget = forms.PasswordInput(
        attrs={'class': 'form-input', 'placeholder': 'nueva contraseña'})
    self.fields['new_password2'].widget = forms.PasswordInput(
        attrs={'class': 'form-input', 'placeholder': 'confirme su contraseña'})
