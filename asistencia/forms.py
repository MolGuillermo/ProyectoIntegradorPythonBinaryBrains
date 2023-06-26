from django import forms
from .models import Beneficiario, Asistencia

class BeneficiarioForm(forms.ModelForm):
    class Meta:
        model = Beneficiario
        fields = ('nombre', 'apellido')

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ('beneficiario', 'fecha', 'presente')