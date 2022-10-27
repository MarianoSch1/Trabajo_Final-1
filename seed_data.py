from viajes.models import Reserva

Reserva(nombre="Rosario", fecha_reserva="05-12-22", hora_reserva="12:20").save()
Reserva(nombre="Alberto", fecha_reserva="15-01-23", hora_reserva="15:31").save()
Reserva(nombre="Samuel", fecha_reserva="12-02-23", hora_reserva="08:54").save()
Reserva(nombre="Florencia", fecha_reserva="28-11-22", hora_reserva="10:45").save()

print("Se cargo con éxito los usuarios de pruebas")