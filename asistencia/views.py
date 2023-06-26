from django.shortcuts import render, get_object_or_404, redirect
from .models import Alumno, Asistencia
from .forms import AlumnoForm, AsistenciaForm

def index(request):
    return render(request, 'asistencia/index.html')

def gestion_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'asistencia/gestion_alumnos.html', {'alumnos': alumnos})

def crear_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestion_alumnos')
    else:
        form = AlumnoForm()
    return render(request, 'asistencia/crear_alumno.html', {'form': form})

def modificar_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('gestion_alumnos')
    else:
        form = AlumnoForm(instance=alumno)
    return render(request, 'asistencia/modificar_alumno.html', {'form': form, 'alumno': alumno})

def eliminar_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == 'POST':
        alumno.delete()
        return redirect('gestion_alumnos')
    return render(request, 'asistencia/eliminar_alumno.html', {'alumno': alumno})

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