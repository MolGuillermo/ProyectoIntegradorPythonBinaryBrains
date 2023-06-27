from django import forms
from .models import Beneficiario, Asistencia

class BeneficiarioForm(forms.ModelForm):
    fecha_de_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    dni = forms.CharField(max_length=20)
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
    
    def clean_dni(self):
        dni = self.cleaned_data.get('dni')
        if not dni:
            raise forms.ValidationError("El campo DNI es obligatorio.")
        return dni

class AsistenciaForm(forms.ModelForm):
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Asistencia
        fields = ('beneficiario', 'fecha', 'presente')