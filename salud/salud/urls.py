from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pacientes.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('especialidades/', include('turnos.urls')),
]
