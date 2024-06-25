from django.shortcuts import render, get_object_or_404
from .models import Paciente, Medico, Especialidad

def inicio(request):
    return render(request, 'pacientes/inicio.html')

def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/lista_pacientes.html', {'pacientes': pacientes})
def lista_medicos(request):
    medicos = Medico.objects.all()
    return render(request, 'pacientes/lista_medicos.html', {'medicos': medicos})

def lista_especialidades(request):
    especialidades = Especialidad.objects.all()
    return render(request, 'turnos/lista_especialidades.html', {'especialidades': especialidades})