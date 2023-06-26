"""
URL configuration for scout project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from asistencia.views import index, gestion_alumnos,crear_alumno,modificar_alumno,eliminar_alumno,gestion_asistencias,crear_asistencia,modificar_asistencia,eliminar_asistencia


urlpatterns = [
    path('', index, name='index'),
    path('alumnos/', gestion_alumnos, name='gestion_alumnos'),
    path('alumnos/crear/', crear_alumno, name='crear_alumno'),
    path('alumnos/modificar/<int:pk>/', modificar_alumno, name='modificar_alumno'),
    path('alumnos/eliminar/<int:pk>/', eliminar_alumno, name='eliminar_alumno'),
    path('asistencias/', gestion_asistencias, name='gestion_asistencias'),
    path('asistencias/crear/', crear_asistencia, name='crear_asistencia'),
    path('asistencias/modificar/<int:pk>/', modificar_asistencia, name='modificar_asistencia'),
    path('asistencias/eliminar/<int:pk>/', eliminar_asistencia, name='eliminar_asistencia'),
]

