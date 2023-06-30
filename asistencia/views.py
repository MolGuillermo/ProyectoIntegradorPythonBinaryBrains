from django.shortcuts import render, get_object_or_404, redirect
from .models import Beneficiario, Asistencia
from .forms import BeneficiarioForm, AsistenciaForm
from django.db.models import Count


# Vista de la página de inicio
def index(request):
    return render(request, 'asistencia/index.html')

# Vista para gestionar los beneficiarios
def gestion_beneficiarios(request):
    # Obtener todos los beneficiarios de la base de datos
    beneficiarios = Beneficiario.objects.all()
    # Renderizar la plantilla 'gestion_beneficiarios.html' y pasar los beneficiarios como contexto
    return render(request, 'asistencia/gestion_beneficiarios.html', {'Beneficiarios': beneficiarios})

# Vista para crear un nuevo beneficiario
def crear_beneficiario(request):
    if request.method == 'POST':
        # Si se recibió una solicitud POST, se crea un formulario con los datos recibidos
        form = BeneficiarioForm(request.POST)
        if form.is_valid():
            # Si el formulario es válido, se guarda en la base de datos
            form.save()
            return redirect('index')
    else:
        # Si no es una solicitud POST, se crea un formulario vacío
        form = BeneficiarioForm()
    # Renderizar la plantilla 'crear_beneficiario.html' y pasar el formulario como contexto
    return render(request, 'asistencia/crear_beneficiario.html', {'form': form})

# Vista para modificar un beneficiario existente
def modificar_beneficiario(request, pk):
    # Obtener el beneficiario con el ID especificado, o mostrar un error 404 si no existe
    beneficiario = get_object_or_404(Beneficiario, pk=pk)
    if request.method == 'POST':
        # Si se recibió una solicitud POST, se crea un formulario con los datos recibidos y el beneficiario existente
        form = BeneficiarioForm(request.POST, instance=beneficiario)
        if form.is_valid():
            # Si el formulario es válido, se guarda en la base de datos
            form.save()
            return redirect('index')
    else:
        # Si no es una solicitud POST, se crea un formulario con los datos del beneficiario existente
        form = BeneficiarioForm(instance=beneficiario)
    # Renderizar la plantilla 'modificar_beneficiario.html' y pasar el formulario y el beneficiario como contexto
    return render(request, 'asistencia/modificar_beneficiario.html', {'form': form, 'beneficiario': beneficiario})

# Vista para eliminar un beneficiario existente
def eliminar_beneficiario(request, pk):
    # Obtener el beneficiario con el ID especificado, o mostrar un error 404 si no existe
    beneficiario = get_object_or_404(Beneficiario, pk=pk)
    if request.method == 'POST':
        # Si se recibió una solicitud POST, se elimina el beneficiario de la base de datos
        beneficiario.delete()
        return redirect('index')
    # Renderizar la plantilla 'eliminar_beneficiario.html' y pasar el beneficiario como contexto
    return render(request, 'asistencia/eliminar_beneficiario.html', {'beneficiario': beneficiario})

# Vista para gestionar las asistencias
def gestion_asistencias(request):
    # Obtener todas las asistencias de la base de datos
    asistencias = Asistencia.objects.all()
    # Renderizar la plantilla 'gestion_asistencias.html' y pasar las asistencias como contexto
    return render(request, 'asistencia/gestion_asistencias.html', {'asistencias': asistencias})

# Vista para crear una nueva asistencia
def crear_asistencia(request):
    if request.method == 'POST':
          # Si se recibió una solicitud POST, se crea un formulario con los datos recibidos
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            # Si el formulario es válido, se guarda en la base de datos
            form.save()
            return redirect('index')
    else:
        # Si no es una solicitud POST, se crea un formulario vacío
        form = AsistenciaForm()
    # Renderizar la plantilla 'crear_asistencia.html' y pasar el formulario como contexto
    return render(request, 'asistencia/crear_asistencia.html', {'form': form})

# Vista para modificar una asistencia existente
def modificar_asistencia(request, pk):
    # Obtener la asistencia con el ID especificado, o mostrar un error 404 si no existe
    asistencia = get_object_or_404(Asistencia, pk=pk)
    if request.method == 'POST':
        # Si se recibió una solicitud POST, se crea un formulario con los datos recibidos y el beneficiario existente
        form = BeneficiarioForm(request.POST, instance=asistencia)
        if form.is_valid():
            # Si el formulario es válido, se guarda en la base de datos
            form.save()
            return redirect('index')
    else:
        # Si no es una solicitud POST, se crea un formulario con los datos de la asistencia existente
        form = AsistenciaForm(instance=asistencia)
    # Renderizar la plantilla 'modificar_asistencia.html' y pasar el formulario y la asistencia como contexto
    return render(request, 'asistencia/modificar_asistencia.html', {'form': form, 'asistencias': asistencia})

# Vista para eliminar una asistencia existente
def eliminar_asistencia(request, pk):
    # Obtener la asistencia con el ID especificado, o mostrar un error 404 si no existe
    asistencia = get_object_or_404(Asistencia, pk=pk)
    if request.method == 'POST':
        # Si se recibió una solicitud POST, se elimina la asistencia de la base de datos
        asistencia.delete()
        return redirect('index')
    # Renderizar la plantilla 'eliminar_asistencia.html' y pasar la asistencia como contexto
    return render(request, 'asistencia/eliminar_asistencia.html', {'asistencia': asistencia})
