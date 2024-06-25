from django.urls import path
from . import views

urlpatterns = [
    # Otras URL patterns
    path('especialidades/<int:especialidad_id>/', views.detalle_especialidad, name='detalle_especialidad'),
    path('especialidades/reserva_turno/<int:especialidad_id>/', views.reserva_turno, name='reserva_turno'),
]
