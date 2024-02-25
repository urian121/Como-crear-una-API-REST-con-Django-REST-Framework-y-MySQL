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
    path('personas/', PersonaList.as_view(), name='persona-list'),
    path('personas/<int:pk>/', PersonaDetail.as_view(), name='persona-detail'),
]
