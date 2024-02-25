'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PersonaListCreate.as_view(),
         name='persona-list-create'),
]
'''

from django.urls import path
from .views import PersonaList, PersonaDetail

urlpatterns = [
    path('', PersonaList.as_view(), name='persona-list'),  # Sin barra al inicio
    path('<int:pk>/', PersonaDetail.as_view(),
         name='persona-detail'),  # Sin barra al inicio
]
