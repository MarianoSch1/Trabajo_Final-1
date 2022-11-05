from django.db import models

class Vuelos(models.Model):
    destino = models.CharField(max_length=100)
    fecha_vuelo = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.destino}, {self.fecha_vuelo}, {self.id}"
