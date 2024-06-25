# En faq/admin.py

from django.contrib import admin
from .models import Pregunta, Categoria

admin.site.register(Pregunta)
admin.site.register(Categoria)
