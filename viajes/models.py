from django.db import models

class Reserva(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_reserva = models.CharField(max_length=200)
    hora_reserva = models.CharField(max_length=200)

def __str__(self):
    return f"{self.nombre}, {self.fecha_reserva}, {self.hora_reserva}, {self.id}"