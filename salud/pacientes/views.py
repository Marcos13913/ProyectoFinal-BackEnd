from django.shortcuts import render
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
    return render(request, 'pacientes/lista_especialidades.html', {'especialidades': especialidades})