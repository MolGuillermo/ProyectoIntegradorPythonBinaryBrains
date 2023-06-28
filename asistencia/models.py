from django.db import models

class Beneficiario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, default="00000000")
    fecha_de_nacimiento = models.DateField(default="2000-01-01")
    edad = models.CharField(max_length=3, default="0")
    rama = models.CharField(max_length=16, choices=(
        ('manada', 'Manada'),
        ('unidad', 'Unidad'),
        ('caminantes', 'Caminantes'),
        ('rovers', 'Rovers'),
        ('adultos', 'Adultos'),
    ), default='manada')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    

class Asistencia(models.Model):
    beneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)
    fecha = models.DateField()
    presente = models.BooleanField(default=False)    

    def __str__(self):
        return f"Asistencia de {self.beneficiario} el {self.fecha}"
    
    