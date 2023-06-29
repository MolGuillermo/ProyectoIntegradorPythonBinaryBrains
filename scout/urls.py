
from django.urls import path
from asistencia import views

urlpatterns = [
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

