from django.db import models
from django.db import models

class Reserva(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_reserva = models.IntegerField()
    hora_reserva = models.IntegerField()

def __str__(self):
    return f"{self.nombre}, {self.fecha_reserva}, {self.hora_reserva}, {self.id}"