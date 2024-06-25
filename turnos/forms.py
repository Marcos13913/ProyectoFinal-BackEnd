from django import forms

class TurnoForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    apellido = forms.CharField(label='Apellido', max_length=100)
    dni = forms.CharField(label='DNI', max_length=10)
    celular = forms.CharField(label='Número de Celular', max_length=20)
    fecha = forms.DateField(label='Fecha del turno', widget=forms.SelectDateWidget)

    def clean_dni(self):
        dni = self.cleaned_data['dni']
        # Validación personalizada para el DNI, si es necesario
        # Por ejemplo:
        if not dni.isdigit() or len(dni) != 8:
            raise forms.ValidationError('El DNI debe ser un número de 8 dígitos.')
        return dni
