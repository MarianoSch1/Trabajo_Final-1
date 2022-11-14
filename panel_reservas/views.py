from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from viajes.models import Reserva
from django import forms

class ReservaList(ListView):
    model= Reserva

class ReservaCrear(CreateView):
    model = Reserva
    success_url= "/panel-reservas/"
    fields= ["nombre", "destino_reserva", "fecha_reserva", "hora_reserva"]
    
    
class ReservaDelete(DeleteView):
    model = Reserva
    success_url = "/panel-reservas/"

class ReservaUpdate(UpdateView):
    model = Reserva
    fields = ["nombre", "destino_reserva", "fecha_reserva", "hora_reserva"]
    success_url =  "/panel-reservas/"