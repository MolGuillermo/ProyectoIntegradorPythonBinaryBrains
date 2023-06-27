from django.db import models

class Beneficiario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=10)
    fecha_de_nacimiento = models.DateField()
    edad = models.CharField(max_length=3)
    rama = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Asistencia(models.Model):
    beneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)
    fecha = models.DateField()
    presente = models.BooleanField(default=False)
    porcentaje = models.FloatField(default=0.0)

    def __str__(self):
        return f"Asistencia de {self.beneficiario} el {self.fecha}"