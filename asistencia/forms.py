from django import forms
from datetime import date
from .models import Beneficiario, Asistencia
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count


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

    def clean_fecha_de_nacimiento(self):
        fecha_nacimiento = self.cleaned_data['fecha_de_nacimiento']
        hoy = date.today()
        edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        
        if edad < 0:
            raise forms.ValidationError("La fecha de nacimiento no puede ser en el futuro.")
        
        return fecha_nacimiento
    
    def clean_dni(self):
        dni = self.cleaned_data.get('dni')
        if not dni:
            raise forms.ValidationError("El campo DNI es obligatorio.")
        return dni
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['class'] = 'centered-form'
        self.fields['apellido'].widget.attrs['class'] = 'centered-form'
        self.fields['dni'].widget.attrs['class'] = 'centered-form'
        self.fields['fecha_de_nacimiento'].widget.attrs['class'] = 'centered-form'
        self.fields['edad'].widget.attrs['class'] = 'centered-form'
        self.fields['rama'].widget.attrs['class'] = 'centered-form'

class AsistenciaForm(forms.ModelForm):
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Asistencia
        fields = ('beneficiario', 'fecha', 'presente')