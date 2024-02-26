from django.contrib import admin

# Importando el modelo Persona
from .models import Persona

# Registrando el modelo Persona en el panel de administración
admin.site.register(Persona)
