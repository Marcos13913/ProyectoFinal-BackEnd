from django.shortcuts import render, get_object_or_404
from .models import Especialidad, Turno
from .forms import TurnoForm

def lista_especialidades(request):
    especialidades = Especialidad.objects.all()
    return render(request, 'turnos/lista_especialidades.html', {'especialidades': especialidades})

from django.shortcuts import render

from django.shortcuts import render
from .forms import TurnoForm

def reserva_turno(request, especialidad_id):

    if request.method == 'POST':
        form = TurnoForm(request.POST)
        if form.is_valid():
            # Procesar los datos del formulario
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            dni = form.cleaned_data['dni']
            celular = form.cleaned_data['celular']
            fecha = form.cleaned_data['fecha']
            # Guardar el turno en la base de datos

            # Redirigir a una página de éxito o donde desees
            return render(request, 'exito.html')
    else:
        form = TurnoForm()

    return render(request, 'reserva_turno.html', {'form': form})


def detalle_especialidad(request, especialidad_id):
    especialidad = get_object_or_404(Especialidad, pk=especialidad_id)
    return render(request, 'detalle_especialidad.html', {'especialidad': especialidad})