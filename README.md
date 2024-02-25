# Cómo crear una API REST con Django REST Framework y MySQL: Paso a paso

##### Descubre Cómo crear una API REST con Django, REST Framework y MySQL. Gestiona datos de base de datos utilizando métodos HTTP (GET, POST, PUT, DELETE) de forma eficiente y segura, proporcionando una interfaz completa para la gestión de información.

#### Dicha API REST con Django REST Framework y MySQL sirve para gestionar datos de personas, incluyendo nombre, edad, sexo, nacionalidad, profesión, y hobby. La API permitirá operaciones CRUD y garantizará la seguridad e integridad de los datos, proporcionando una interfaz robusta y escalable para su uso.

1.  Crear un entorno virtual, hay muchas formas

        Opción 1: Crear entorno virtual con el paquete virtualenv
        Si no tienes instalado virtualenv puedes instalarlo de forma global en el sistema atraves de https://pypi.org/project/virtualenv/
        pip install virtualenv -> Instalar de forma global
        virtualenv env -> Crear entorno
        virtualenv --version -> Ver la versión de virtualenv

        Opción 2: Crear un entorno virtual con el paquete que ya viene por defecto en las ultimas versiones de Python
        python -m venv env

2.  Activar entorno virtual

        . env/Script/activate -> Para Windows
        . env/bin/activate -> Para Mac
        deactivate --> Para desactivar mi entorno virtual

3.  Instalar django desde el manejador de paquete de Python Pip, ya dentro del entorno virtual

        pip install Django
        Nota: para instalar Django en una versión especifica
        pip install Django==4.2.4

4.  Ver la versión de Django instalada en el proyecto

        python -m django --version

5.  Instalar el controlador de MySQL, driver para conectar Gestor de BD MySQL con Django

        pip install mysqlclient

6.  Instalación de Django REST Framework, el cual nos va permitir hacer todas las solicitudes HTTP

        pip install django djangorestframework

7.  Crear el proyecto con django

        `django-admin startproject project_core .`
        El punto . es crucial, le dice al script que cree el proyecto de Django en el directorio actual

8.  Correr el proyecto 'project_core' de Django que hemos creado

        python manage.py runserver 8500

9.  Crear mi primera aplicación en Django

        python manage.py startapp api_personas

10. Instalar la aplicación (api_personas) ya creada en el proyecto, en el archivo settings.py y instalar también (rest_framework)

        archivo settings.py
        INSTALLED_APPS = [
                ----,
                'rest_framework'
                'api_personas',
        ]

11. Editar el archivo settings.py del proyecto, cambiando los parametros de conexión a MySQL

        DATABASES = {
                'default': {
                        'ENGINE': 'django.db.backends.mysql', #ENGINE es motor de BD
                        'NAME': 'api_django_rest_framework',
                        'USER': 'root',
                        'PASSWORD': '',
                        'HOST': '127.0.0.1',
                        'PORT': '3306',
                }
        }

12. Crear una clase en models.py la cuál representará mi tabla en BD,(bd_django) preferiblemente los modelos
    se declaran en singular

        class Persona(models.Model):
                nombre = models.CharField(max_length=100)
                edad = models.IntegerField()
                sexo = models.CharField(max_length=1, choices=(('M', 'Masculino'), ('F', 'Femenino')))
                nacionalidad = models.CharField(max_length=100)
                profesion = models.CharField(max_length=100)
                hobby = models.CharField(max_length=100)
                created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
                updated = models.DateTimeField(auto_now_add=False, auto_now=True)

13. Crear la Base de Datos (api_django_rest_framework) en el gestor de BD MySQL

14. Crear y correr las migraciones

        python manage.py makemigrations -> Creando migraciones
        python manage.py migrate         -> Correr migraciones

15. Correr el proyecto

        python manage.py runserver 8500
        Revisar la consola y visitar la URL http://127.0.0.1:8000

16. Para administrar personas desde el panel de Django, crea un usuario de Cpanel utilizando el siguiente comando

        python manage.py createsuperuser

17. Registrar mi modelo (Persona) en Django Admin, editar el archivo admin.py de mi aplicación

        from .models import Persona
        admin.site.register(Persona)

18. Crear el archivo urls.py en la aplicación (bd_django_mysql)

        from django.urls import path
        from . import views

                urlpatterns = [
                        path('', views.inicio, name='inicio'),
                        path('registrar_empleado/', views.registrar_empleado,
                                name='registrar_empleado'),
                        path('empleados/', views.list´ar_empleados, name='listar_empleados'),
                ]

19. Conectar las URLS de mi aplicación con el projecto, para esto vamos al archivo uls.py del projecto
    from django.urls import path, include

        urlpatterns = [
                path('admin/', admin.site.urls),
                path("", include('empleados.urls'))
        ]

20. Crear la carpeta 'templates' dentro de la aplicación donde estarán mis archivos.html

21. Crear la carpeta 'static' dentro de mi aplicacion, aqui estaran archivos
    estaticos (css, js, imagenes, etc..)

22. Crear la carpeta media, para almacenar las imagenes del empleado

23. Correr archivo requirement.txt

        pip install -r requirements.txt

24. Crear el archivo requirements.txt para tener todos los paquetes del proyecto a la mano

        pip freeze > requirements.txt

        Nota: para instalar los paquetes solo basta ejecutar
        pip install -r requirements.txt

#### Resultado final

#####Formulario para registrar Empleado
![](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/master/registrar-empleado-con-django-crud-urian-viera.png)

##### Lista de Empleados

![](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/master/lista-de-empleados-crud-django-urian-viera.png)

### Expresiones de Gratitud 🎁

    Comenta a otros sobre este proyecto 📢
    Invita una cerveza 🍺 o un café ☕
    Paypal iamdeveloper86@gmail.com
    Da las gracias públicamente 🤓.

## No olvides SUSCRIBIRTE 👍
