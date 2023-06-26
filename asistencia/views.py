from django.shortcuts import render, get_object_or_404, redirect
from .models import Beneficiario, Asistencia
from .forms import BeneficiarioForm, AsistenciaForm

def index(request):
    return render(request, 'asistencia/index.html')

def gestion_beneficiarios(request):
    beneficiarios = Beneficiario.objects.all()
    return render(request, 'asistencia/gestion_beneficiarios.html', {'beneficiarios': beneficiarios})

def crear_beneficiario(request):
    if request.method == 'POST':
        form = BeneficiarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestion_beneficiarios')
    else:
        form = BeneficiarioForm()
    return render(request, 'asistencia/crear_beneficiario.html', {'form': form})

def modificar_beneficiario(request, pk):
    beneficiario = get_object_or_404(Beneficiario, pk=pk)
    if request.method == 'POST':
        form = BeneficiarioForm(request.POST, instance=beneficiario)
        if form.is_valid():
            form.save()
            return redirect('gestion_beneficiarios')
    else:
        form = BeneficiarioForm(instance=beneficiario)
    return render(request, 'asistencia/modificar_beneficiario.html', {'form': form, 'beneficiario': beneficiario})

def eliminar_beneficiario(request, pk):
    beneficiario = get_object_or_404(Beneficiario, pk=pk)
    if request.method == 'POST':
        beneficiario.delete()
        return redirect('gestion_beneficiario')
    return render(request, 'asistencia/eliminar_beneficiario.html', {'beneficiario': beneficiario})

def gestion_asistencias(request):
    asistencias = Asistencia.objects.all()
    return render(request, 'asistencia/gestion_asistencias.html', {'asistencias': asistencias})

def crear_asistencia(request):
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestion_asistencias')
    else:
        form = AsistenciaForm()
    return render(request, 'asistencia/crear_asistencia.html', {'form': form})

def modificar_asistencia(request, pk):
    asistencia = get_object_or_404(Asistencia, pk=pk)
    if request.method == 'POST':
        form = AsistenciaForm(request.POST, instance=asistencia)
        if form.is_valid():
            form.save()
            return redirect('gestion_asistencias')
    else:
        form = AsistenciaForm(instance=asistencia)
    return render(request, 'asistencia/modificar_asistencia.html', {'form': form, 'asistencia': asistencia})

def eliminar_asistencia(request, pk):
    asistencia = get_object_or_404(Asistencia, pk=pk)
    if request.method == 'POST':
        asistencia.delete()
        return redirect('gestion_asistencias')
    return render(request, 'asistencia/eliminar_asistencia.html', {'asistencia': asistencia})