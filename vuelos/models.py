from django.db import models

class Vuelos(models.Model):
    class DestinoChoices(models.TextChoices):
        Bogota = "Bogotá"
        Caracas =  "Caracas"
        Rio_de_Janeiro =  "Río de Janeiro"
        Montevideo = "Montevideo"
        Bariloche = "San Carlos de Bariloche"
        Iguazu = "Puerto Iguazú"
        Mendoza = "Mendoza"
    nombre_pasajero = models.CharField(max_length=200)
    destino = models.CharField(max_length=100, choices= DestinoChoices.choices, default=DestinoChoices.Bogota)
    fecha_vuelo_ida = models.CharField(max_length=100, default="")
    fecha_vuelo_vuelta= models.CharField(max_length=100, default="")
    
    def __str__(self):
        return f"{self.nombre_pasajero}, {self.destino}, {self.fecha_vuelo_ida}, {self.fecha_vuelo_vuelta},{self.id}"
