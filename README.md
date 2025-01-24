# Cómo Crear una API REST con Django REST Framework y MySQL: Paso a Paso 

Esta guía te enseña cómo crear una **API RESTful** con Django, **Django REST Framework** (***DRF***) y MySQL para gestionar datos relacionados con personas, como nombre, edad, sexo, nacionalidad, profesión y hobby. Implementa operaciones CRUD (Crear, Leer, Actualizar, Eliminar) de manera eficiente y segura. 

## Requisitos Previos 
Antes de comenzar, asegúrate de tener instalados los siguientes componentes en tu sistema:  
- Python 3.x 
- MySQL 
- pip (gestor de paquetes de Python)  

## Paso 1: 
Crear un Entorno Virtual  Primero, crea un entorno virtual para tu proyecto.

### Opción 1: Usando `virtualenv` 
```bash
pip install virtualenv 
Instalar virtualenv globalmente virtualenv env  # Crear entorno virtual
virtualenv --version  # Ver versión de virtualenv
```

### Opción 2: Usando `venv` (incluido en Python)
```bash
python -m venv env  # Crear entorno virtual
```


Paso 2: Activar el Entorno Virtual
----------------------------------

### En Windows:

```bash
.\env\Scripts\activate
### En macOS/Linux:
source env/bin/activate
### Para desactivar el entorno virtual:
deactivate
```

Paso 3: Instalar Django
-----------------------

Con el entorno virtual activado, instala Django:
`pip install Django`

Si necesitas una versión específica de Django:
`pip install Django==4.2.4`

Paso 4: Verificar la Versión de Django
--------------------------------------

Para verificar que Django está correctamente instalado:
`python -m django --version`

Paso 5: Instalar el Controlador de MySQL
----------------------------------------

Instala el paquete necesario para conectar Django con MySQL:
`pip install mysqlclient`


Paso 6: Instalar Django REST Framework
--------------------------------------

Django REST Framework es la librería que te permitirá manejar las solicitudes HTTP en tu API.

`pip install djangorestframework`

Paso 7: Crear el Proyecto Django
--------------------------------

Crea el proyecto base de Django:
`django-admin startproject project_core .`

Nota: El `.` al final crea el proyecto en el directorio actual.


Paso 8: Ejecutar el Proyecto
----------------------------

Inicia el servidor de desarrollo de Django:
`python manage.py runserver 8500`

Accede a la URL `http://127.0.0.1:8500` en tu navegador.

Paso 9: Crear la Aplicación de Personas
---------------------------------------

Crea una nueva aplicación en tu proyecto Django:

`python manage.py startapp api_personas`

* * *

Paso 10: Instalar la Aplicación en el Proyecto
----------------------------------------------

Agrega la aplicación y Django REST Framework en el archivo `settings.py`:

```bash
INSTALLED_APPS = [
    ...
    'rest_framework',
    'api_personas',
]
```

Paso 11: Configuración de la Conexión a MySQL
---------------------------------------------

Configura la conexión a la base de datos en `settings.py`:

```bash
`DATABASES = {     
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


Paso 12: Crear la Base de Datos en MySQL
----------------------------------------

Crea la base de datos `api_django_rest_framework` en tu gestor de bases de datos MySQL.

Paso 13: Crear los Modelos en Django
------------------------------------

Define el modelo `Persona` en `models.py`:
```bash
    generos = (
        ("M", "Masculino"),
        ("F", "Femenino"),
        ("Otro", "Otro"),
    )

    class Persona(models.Model):
        nombre = models.CharField(max_length=100)
        edad = models.IntegerField()
        sexo = models.CharField(max_length=5, choices=generos)
        nacionalidad = models.CharField(max_length=100)
        profesion = models.CharField(max_length=100)
        hobby = models.CharField(max_length=100)
        created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
        updated = models.DateTimeField(auto_now=True)

        def __str__(self):
            return f"{self.id} - {self.nombre} - {self.edad} - {self.sexo} - {self.nacionalidad} - {self.profesion} - {self.hobby}"

        class Meta:
            db_table = "tbl_personas"
            ordering = ['-created_at']
```

Paso 14: Crear y Correr las Migraciones
---------------------------------------

Genera y ejecuta las migraciones para crear las tablas en la base de datos:
`python manage.py makemigrations python manage.py migrate`

Paso 15: Ejecutar el Proyecto
-----------------------------

Ejecuta nuevamente el servidor:
`python manage.py runserver 8500`

Paso 16: Crear un Usuario para el Panel de Django
-------------------------------------------------

Para administrar los datos desde el panel de Django, crea un superusuario:
`python manage.py createsuperuser`


Paso 17: Acceder al Panel de Administración de Django
-----------------------------------------------------

Accede al panel de administración de Django en `http://127.0.0.1:8500/admin`.

Paso 18: Registrar el Modelo en Django Admin
--------------------------------------------

Registra el modelo `Persona` en el panel de administración:

```bash
from django.contrib import admin
from .models import Persona

admin.site.register(Persona)
```

Paso 19: Crear el Serializador
------------------------------

Crea un archivo `serializers.py` en tu aplicación y define el serializador para convertir los objetos de `Persona` a JSON:

```bash
from rest_framework import serializers
from .models import Persona

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

```

Paso 20: Crear Vistas con Django REST Framework
-----------------------------------------------

Define las vistas que manejarán las operaciones CRUD en `views.py`:

```bash
from rest_framework import generics
from .models import Persona
from .serializers import PersonaSerializer

class PersonaListCreate(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
```

Paso 21: Crear las Rutas de la API
----------------------------------

Define las rutas en `urls.py` de la aplicación `api_personas`:

```bash
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PersonaListCreate.as_view(), name='persona-list-create'),
]
```


Paso 22: Conectar las Rutas con el Proyecto
-------------------------------------------

Agrega las rutas de la aplicación al archivo `urls.py` del proyecto:

```bash
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/personas/', include('api_personas.urls')),
]
```


Paso 23: Instalar Dependencias desde el `requirements.txt`
----------------------------------------------------------

Si tienes un archivo `requirements.txt`, instala todas las dependencias:
`pip install -r requirements.txt`


Resultado Final
---------------

Una vez completados los pasos, tu API estará lista para realizar las operaciones CRUD sobre los datos de `Persona`. Puedes interactuar con la API desde las siguientes rutas:

*   `http://127.0.0.1:8500/api/personas/` - Para listar o agregar personas (GET, POST).
*   `http://127.0.0.1:8500/api/personas/1/` - Para obtener, actualizar o eliminar una persona específica (GET, PUT, DELETE).

![Diagrama API Django REST](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/master/Django-REST-framework.png)

* * *

Expresiones de Gratitud 🎁
--------------------------

*   Comenta sobre este proyecto 📢
*   Invita una cerveza 🍺 o un café ☕ Paypal
*   Da las gracias públicamente 🤓.


Notas
-----

*   **Routers**: Permiten definir las URLs de tu API de manera sencilla y ordenada, encaminando las solicitudes a los métodos correspondientes según el verbo HTTP (GET, POST, PUT, PATCH).
*   **Vistas en Django**: En lugar de renderizar HTML, las vistas de Django devuelven JSON, XML u otros formatos de datos para tu API.
*   **ViewSets**: Son un tipo especial de vista que facilita la definición de múltiples operaciones CRUD de forma más compacta.
*   **Serializadores**: Permiten definir cómo deben ser estructurados los datos en las respuestas de tu API y cómo se procesan los datos en las solicitudes.
*   **Generics**: `ListCreateAPIView` es una vista genérica que soporta las operaciones de listar y crear de manera automática.

* * *

Documentación Adicional
-----------------------

*   [Documentación Oficial de Django REST Framework](https://www.django-rest-framework.org/)
*   [Documentación Adicional](https://piptocode.github.io/manuals/frameworks/djangorest.html)

