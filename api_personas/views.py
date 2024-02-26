'''
from rest_framework import generics
from .models import Persona
from .serializers import PersonaSerializer


class PersonaListCreate(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    # establece el serializador que se utilizará para convertir instancias del modelo Persona en formatos de datos como JSON, XML, etc
    serializer_class = PersonaSerializer
'''


from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Persona
from .serializers import PersonaSerializer
# Crear una separación y control sobre cada método HTTP (GET, POST, PUT, DELETE) en tu API.


# Esta clase maneja las operaciones que implican una lista de recursos del modelo Persona. Normalmente, incluye métodos para manejar solicitudes HTTP como GET (para recuperar una lista de personas) y POST (para crear una nueva persona).
class PersonaList(APIView):
    # GET: Obtiene todas las personas
    def get(self, request):
        personas = Persona.objects.all()
        serializer = PersonaSerializer(personas, many=True)
        return Response(serializer.data)

    # POST: Crea una nueva persona
    def post(self, request):
        serializer = PersonaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Esta clase se encarga de las operaciones relacionadas con un recurso individual del modelo Persona. Generalmente, incluye métodos para manejar solicitudes HTTP como GET (para recuperar los detalles de una persona), PUT (para actualizar una persona existente) y DELETE (para eliminar una persona).
class PersonaDetail(APIView):
    # Obtiene una persona específica por su id
    def get_object(self, pk):
        return get_object_or_404(Persona, pk=pk)

    # GET: Obtiene detalles de una persona por su ID
    def get(self, request, pk):
        persona = self.get_object(pk)
        serializer = PersonaSerializer(persona)
        return Response(serializer.data)

    # PUT: Actualiza los detalles de una persona
    def put(self, request, pk):
        persona = self.get_object(pk)
        serializer = PersonaSerializer(persona, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE: Elimina una persona
    def delete(self, request, pk):
        persona = self.get_object(pk)
        persona.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
