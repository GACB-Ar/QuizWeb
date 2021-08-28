from django.shortcuts import redirect, render
from .forms import EditarPerfilForm, NuevoPerfilForm, IniciarSesionForm, CambiarPassword
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required


# Create your views here.
def crear_usuario(request):
  if request.user.is_authenticated:
    return redirect("inicio")
  
  form = NuevoPerfilForm(request.POST or None)
  if request.method == "POST":
    if form.is_valid():
      user = form.save()
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


@login_required
def pass_cambiada(request):
  form = CambiarPassword(request.user)

  if request.method == 'POST':
    form = CambiarPassword(request.user, request.POST)
    if form.is_valid():
      form.user.set_password(form.cleaned_data["new_password1"])
      form.save()
      update_session_auth_hash(request, request.user)
      return redirect("inicio")
  contexto = {"form": form}
  return render(request, "cuenta/cambiar_pass.html", contexto)


def iniciar_sesion(request):
  form = IniciarSesionForm()
  if request.method == "POST":
    form = IniciarSesionForm(data=request.POST)
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
