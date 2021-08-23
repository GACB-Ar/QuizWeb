from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class PerfilAdmin(UserAdmin):
  # search_fields = ['username', 'first_name', 'last_name']
  list_display = [
    'username', 'first_name',
    'last_name', 'email', 'puntaje',
    'is_staff', 'is_superuser']

  fieldsets = (
    ('Usuario',
      {'fields': ('username', 'password')}),
    ('Información Personal',
      {'fields': (
        'first_name',
        'last_name',
        'email',
      )}),
    ("otros datos",
      {'fields': (
        'puntaje',
      )}),
    ('Permisos',
      {'fields': (
        'is_active',
        'is_staff',
        'is_superuser',
      )}),
  )


# Register your models here.
admin.site.register(Perfil, PerfilAdmin)
