# 🚀 API REST con Django REST Framework y MySQL (CRUD)

Esta guía muestra cómo crear una **API RESTful** usando **Django**, **Django REST Framework (DRF)** y **MySQL** para gestionar información de personas (nombre, edad, sexo, nacionalidad, profesión y hobby), implementando un **CRUD completo**, claro y escalable.


## 🧰 Stack usado

* Python 3.x
* Django
* Django REST Framework
* MySQL

## 📋 Requisitos previos

Antes de empezar, asegúrate de tener:

* Python 3.x
* MySQL
* pip


## ⚙️ Paso 1: Crear entorno virtual

### Opción 1: `virtualenv`

```bash
pip install virtualenv
virtualenv env
virtualenv --version
```

### Opción 2: `venv` (recomendado)

```bash
python -m venv env
```

## ▶️ Paso 2: Activar entorno virtual

### Windows

```bash
.\env\Scripts\activate
```

### macOS / Linux

```bash
source env/bin/activate
```

Para desactivar:

```bash
deactivate
```


## 📦 Paso 3: Instalar dependencias

```bash
pip install Django djangorestframework mysqlclient
```

Versión específica (opcional):

```bash
pip install Django==4.2.4
```

Verificar instalación:

```bash
python -m django --version
```

## 🏗️ Paso 4: Crear proyecto Django

```bash
django-admin startproject project_core .
```

> El `.` crea el proyecto en el directorio actual.


## ▶️ Paso 5: Ejecutar servidor

```bash
python manage.py runserver 8500
```

Abrir 👉 `http://127.0.0.1:8500`


## 📁 Paso 6: Crear app de personas

```bash
python manage.py startapp api_personas
```

## ⚙️ Paso 7: Registrar apps (`settings.py`)

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'api_personas',
]
```

## 🛢️ Paso 8: Configurar MySQL

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'api_django_rest_framework',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

Crear la base de datos en MySQL:

```sql
CREATE DATABASE api_django_rest_framework;
```


## 🧩 Paso 9: Modelo `Persona`

```python
class Persona(models.Model):
    GENEROS = (
        ("M", "Masculino"),
        ("F", "Femenino"),
        ("O", "Otro"),
    )

    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=5, choices=GENEROS)
    nacionalidad = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)
    hobby = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tbl_personas"
        ordering = ['-created_at']

    def __str__(self):
        return self.nombre
```


## 🔄 Paso 10: Migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

## 👤 Paso 11: Crear superusuario

```bash
python manage.py createsuperuser
```

Acceder al admin 👉
`http://127.0.0.1:8500/admin`

Registrar modelo:

```python
admin.site.register(Persona)
```


## 🔄 Paso 12: Serializador

```python
from rest_framework import serializers
from .models import Persona

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'
```

## 🧠 Paso 13: Vistas (CRUD)

```python
from rest_framework.generics import ListCreateAPIView
from .models import Persona
from .serializers import PersonaSerializer

class PersonaListCreate(ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
```

## 🌐 Paso 14: URLs de la app

```python
from django.urls import path
from .views import PersonaListCreate

urlpatterns = [
    path('', PersonaListCreate.as_view(), name='personas'),
]
```

Conectar al proyecto:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/personas/', include('api_personas.urls')),
]
```


## 📌 Endpoints disponibles

| Método | Endpoint              | Acción          |
| ------ | --------------------- | --------------- |
| GET    | `/api/personas/`      | Listar personas |
| POST   | `/api/personas/`      | Crear persona   |
| PUT    | `/api/personas/{id}/` | Actualizar      |
| DELETE | `/api/personas/{id}/` | Eliminar        |


## 🖼️ Diagrama

![Django REST API](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/master/Django-REST-framework.png)


## 🧠 Notas importantes

* Usa **Generics** para reducir código repetido
* DRF devuelve **JSON**, no HTML
* Puedes mejorar usando **ViewSets + Routers**
* Ideal agregar **JWT y permisos** en producción


## 📚 Documentación

* 🔗 [https://www.django-rest-framework.org/](https://www.django-rest-framework.org/)
* 🔗 [https://piptocode.github.io/manuals/frameworks/djangorest.html](https://piptocode.github.io/manuals/frameworks/djangorest.html)


## ☕ Agradecimientos

Si te sirvió:

* ⭐ Dale star al repo
* ☕ Invita un café
* 📢 Comparte el proyecto
