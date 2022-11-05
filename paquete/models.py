from django.db import models

class Paquete(models.Model):
    destino = models.CharField(max_length=100)
    fecha_ida= models.CharField(max_length=200)
    fecha_vuelta = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.destino}, {self.fecha_ida}, {self.fecha_vuelta}, {self.id}"
