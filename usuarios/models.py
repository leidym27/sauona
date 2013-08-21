from django.db import models

# Create your models here.
class Usuario(models.Model):
    """Modelo Usuario"""
    correlativo = models.IntegerField()
    apellidos = models.CharField(max_length=200)
    nombres = models.CharField(max_length=200)
    cedula = models.CharField(max_length=12)
    nacionalidad = models.BooleanField()
    sexo = models.BooleanField()
    fecha_nacimiento = models.DateField()
    lugar_nacimiento = models.CharField(max_length=200)
    estado_nacimiento = models.CharField(max_legth=50)
    pais = models.CharField(max_length=100)
    referido = models.CharField(max_length=50)
    nivel_educativo = models.CharField(max_length=50)
    asiste_oficina = models.BooleanField()
    acompanante = models.CharField(max_length=50)
    decision_asistir = models.BooleanField()
    razon = models.TextField()
    profesion = models.CharField(max_length=50)
    historia_laboral = models.CharField(max_length=100)
    ocupacion_actual = models.CharField(max_length=100)
    estado_civil = models.CharField(max_length=100)
    direccion_habitacion = models.TextField()
    zona = models.CharField(max_length=100)
    parroquia = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    zona_postal = models.CharField(max_length=4)
    telefono = models.CharField(max_length=12)
    celular = models.CharField(max_length=12)
    
            