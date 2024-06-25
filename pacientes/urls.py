from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('pacientes/', views.lista_pacientes, name='lista_pacientes'),
    path('medicos/', views.lista_medicos, name='lista_medicos'),
    path('especialidades/', views.lista_especialidades, name='lista_especialidades'),
]
