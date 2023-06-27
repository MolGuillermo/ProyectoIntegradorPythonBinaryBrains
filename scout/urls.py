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
# from asistencia.views import index, gestion_beneficiarios,crear_beneficiario,modificar_beneficiario,eliminar_beneficiario,gestion_asistencias,crear_asistencia,modificar_asistencia,eliminar_asistencia
from asistencia import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('beneficiarios/', views.gestion_beneficiarios, name='gestion_beneficiarios'),
    path('beneficiarios/crear/', views.crear_beneficiario, name='crear_beneficiario'),
    path('beneficiarios/modificar/<int:pk>/', views.modificar_beneficiario, name='modificar_beneficiario'),
    path('beneficiario/eliminar/<int:pk>/', views.eliminar_beneficiario, name='eliminar_beneficiario'),
    path('asistencias/', views.gestion_asistencias, name='gestion_asistencias'),
    path('asistencias/crear/', views.crear_asistencia, name='crear_asistencia'),
    path('asistencias/modificar/<int:pk>/', views.modificar_asistencia, name='modificar_asistencia'),
    path('asistencias/eliminar/<int:pk>/', views.eliminar_asistencia, name='eliminar_asistencia'),
]

