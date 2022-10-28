from django.db import models

class Reserva(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_reserva = models.CharField(max_length=200)
    hora_reserva = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.nombre}, {self.fecha_reserva}, {self.hora_reserva}, {self.id}"

class vuelos(models.Model):
    destino = models.CharField(max_length=100)
    fecha_vuelo = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.destino}, {self.fecha_vuelo}, {self.id}"

class Paquete(models.Model):
    destino = models.CharField(max_length=100)
    fecha_ida= models.CharField(max_length=200)
    fecha_vuelta = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.destino}, {self.fecha_ida}, {self.fecha_vuelta}, {self.id}"