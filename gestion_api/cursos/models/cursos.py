from django.db import models

class Cursos(models.Model):
    codigo = models.CharField(max_length=120, unique=True)
    titulo = models.CharField(max_length=140, unique=True)
    subtitulo = models.CharField(max_length=120, unique=True)
    descripcion = models.CharField(max_length=300, unique=True)
    nivel  = models.CharField(max_length=120, unique=True)
    duracion_horas = models.PositiveIntegerField(default=0)
    costo  = models.DecimalField(max_digits=10, decimal_places=2)
    modalidad = models.CharField(max_length=120, unique=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=120, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.titulo