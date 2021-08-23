from django.urls import path
from . import views
from django.contrib.auth import views as auth_user_views

urlpatterns = [
  #login
  path(
    "iniciar_sesion/",
    auth_user_views.LoginView.as_view(
      template_name="cuenta/login.html",
    ),
    name="iniciar_sesion"
  ),

  #logout
  path(
    "cerrar_sesion/",
    auth_user_views.LogoutView.as_view(),
    name="cerrar_sesion"
  ),

  #registrar usuario
  path(
    "crear_usuario",
    views.crear_usuario,
    name="crear_usuario"
  ),
  
  #editar usuario
  path(
    "editar_usuario/",
    views.editar_usuario,
    name="editar_usuario"
  ),

  #cambiar contraseña
  path(
      "cambiar_pass/",
    auth_user_views.PasswordChangeView.as_view(
      template_name="cuenta/cambiar_pass.html"
    ),
    name="change_password"
  ),
  path("cambiado/", views.pass_cambiada, name="password_change_done")
]
