from django import forms
from .models import Beneficiario, Asistencia

class BeneficiarioForm(forms.ModelForm):
    rama = forms.ChoiceField(choices=(
        ('manada', 'Manada'),
        ('unidad', 'Unidad'),
        ('caminantes', 'Caminantes'),
        ('rovers', 'Rovers'),
        ('adultos', 'Adultos'),
    ))

    class Meta:
        model = Beneficiario
        fields = ('nombre', 'apellido', 'dni', 'fecha_de_nacimiento', 'edad','rama')

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ('beneficiario', 'fecha', 'presente', 'porcentaje')