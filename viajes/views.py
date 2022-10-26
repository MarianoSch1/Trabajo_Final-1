from django.shortcuts import render
from viajes.models import Reserva
from viajes.forms import Buscar
from django.views import View

def mostrar_reserva(request):
  lista_reservas = Reserva.objects.all()
  return render(request, "viajes/rervas.html", {"lista_reservas": lista_reservas})

class BuscarReserva(View):

    form_class = Buscar
    template_name = 'viajes/buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_reservas = Reserva.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_reservas':lista_reservas})
        return render(request, self.template_name, {"form": form})
