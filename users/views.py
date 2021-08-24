from django import forms
from django.shortcuts import redirect, render, resolve_url
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import EditarPerfilForm, NuevoPerfilForm, CambiarPassword
from .models import Perfil
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.password_validation import password_changed
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required

# Create your views here.
#parte del front
def inicio_de_sesion(request):
  # if request.user.is_authenticated: #and request.user.is_staff:
  #   template = "admin_dashboard.html"
  # else:
  template = "inicio_de_sesion.html"
  contexto = {}
  return render(request, template, contexto)

def formulario(request):
  # if request.user.is_authenticated: #and request.user.is_staff:
  #   template = "admin_dashboard.html"
  # else:
  template = "formulario.html"
  contexto = {}
  return render(request, template, contexto)

#hasta aca es front


def crear_usuario(request):
  if request.user.is_authenticated:
    return redirect("inicio")
  form = NuevoPerfilForm(request.POST or None)
  if request.method == "POST":
    if form.is_valid():
      user = form.save()
      #return redirect("iniciar_sesion")
      login(request, user)

      return redirect("inicio")
  contexto = {"form": form}
  return render(request, "cuenta/nuevo_usuario.html", contexto)


def editar_usuario(request):
  if not request.user.is_authenticated:
    return redirect("iniciar_sesion")

  perfil = request.user
  form = EditarPerfilForm(instance=perfil)
  if request.method == "POST":
    form = EditarPerfilForm(request.POST, instance=perfil)
    if form.is_valid():
      form.save()
      return redirect("inicio")
  contexto = {"form": form}
  return render(request, "cuenta/editar_usuario.html", contexto)


def iniciar_sesion(request):
  form = AuthenticationForm()
  if request.method == "POST":
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
      username = form.cleaned_data["username"]
      password = form.cleaned_data["password"]
      user = authenticate(username=username, password=password)
      login(request, user)

      return redirect("inicio")

    print("errores: ", form.errors)
  contexto = {"form": form}
  return render(request, "cuenta/login.html", contexto)


def cerrar_sesion(request):
  if request.user.is_authenticated():
    logout(request, request.user)
  return redirect("inicio")



@login_required
def pass_cambiada(request):
  form = CambiarPassword(request.user)

  if request.method == 'POST':
    form = CambiarPassword(request.user, request.POST)
    if form.is_valid():
      user = Perfil.objects.get(username=form.user.cleaned_data["username"])
      password = form.cleaned_data["new_password1"]
      form.user.set_password(password)
      form.save()
      update_session_auth_hash(request, user)

  contexto = {"form": form}
  return render(request, "cuenta/cambiar_pass.html", contexto)