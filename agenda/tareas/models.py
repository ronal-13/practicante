from django.db import models

class Tarea(models.Model):
    PRIORIDAD_CHOICES = [
        (1, 'Baja'),
        (2, 'Media'),
        (3, 'Alta'),
    ]
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En progreso'),
        ('completada', 'Completada'),
    ]
    
    titulo = models.CharField(max_length=100)
    prioridad = models.IntegerField(choices=PRIORIDAD_CHOICES)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    fecha_limite = models.DateField()

    def __str__(self):
        return self.titulo
    
# Create your models here.
