# En faq/views.py

from django.views.generic import ListView, DetailView
from .models import Pregunta

class ListaPreguntas(ListView):
    model = Pregunta
    template_name = 'faq/lista_preguntas.html'
    context_object_name = 'preguntas'

class DetallePregunta(DetailView):
    model = Pregunta
    template_name = 'faq/detalle_pregunta.html'
    context_object_name = 'pregunta'
