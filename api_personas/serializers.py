# Importación de módulos y clases necesarias
from rest_framework import serializers
from .models import Persona  # Importar modelo Persona


# Definición del serializador, se utiliza una clase llamada PersonaSerializer que hereda de serializers.ModelSerializer.
# Este serializador se utilizará para convertir instancias del modelo Persona a formatos de datos que puedan ser fácilmente representados y transmitidos, como JSON.
class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'  # Para obtener todos los campos
        # fields = ['id', 'nombre', 'edad', 'sexo','nacionalidad', 'profesion', 'hobby']
