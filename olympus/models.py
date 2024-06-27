from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    duracion = models.DurationField()  # Duración del servicio

    def __str__(self):
        return self.nombre


class Reserva(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=20, default='Pendiente')



    def __str__(self):
        return f"{self.usuario.username} - {self.servicio.nombre} - {self.fecha} {self.hora}"
    
class CustomUser(AbstractUser):
    rut = models.CharField(max_length=12, unique=True)
#----------------------------------------------------------------------------
