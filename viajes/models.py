from django.db import models

class Reserva(models.Model):
    nombre = models.CharField(max_length=100)
    class Destino(models.TextChoices):
        Ibis_Bogota = "Hotel Ibis Bogota Museo, 6 noches + aereo"
        CCT_Caracas =  "Hotel CCT Caracas, 6 noches + aereo"
        Vila_Santa_Teresa_Rio_de_Janeiro =  "Hotel Vila Santa Teresa Río de Janeiro, 6 noches + aereo"
        FAUNA_Montevideo = "Hotel FAUNA Montevideo, 6 noches + aereo"
        Huinid_Pioneros_Bariloche = "Hotel Huinid Pioneros San Carlos de Bariloche, 6 noches + aereo"
        Alma_Pura_Iguazu = "Hotel Alma Pura Puerto Iguazú, 6 noches + aereo"
        Raices_Aconcagua_Mendoza = "Hotel Raices Aconcagua Mendoza, 6 noches + aereo"
    destino_reserva = models.CharField(max_length=100, choices= Destino.choices, default=Destino.Ibis_Bogota)
    fecha_reserva = models.CharField(max_length=100)
    hora_reserva = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nombre}, {self.destino_reserva}, {self.fecha_reserva}, {self.hora_reserva}, {self.id}"
