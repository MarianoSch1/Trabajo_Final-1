from django.shortcuts import render
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from viajes.models import Reserva
from django.views import View
from viajes.forms import Buscar, ReservaForm
from django.views.generic import DeleteView

def mostrar_reserva(request):
  lista_reservas = Reserva.objects.all()
  return render(request, "viajes/reservas.html", {"lista_reservas": lista_reservas})

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

class AltaReserva(View):
    
    form_class = ReservaForm
    template_name = 'viajes/alta_reserva.html'
    initial = {"nombre":"", "destino_reserva":"", "fecha_reserva":"", "hora_reserva":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"Se cargo con éxito la reserva de {form.cleaned_data.get('nombre')}, a {form.cleaned_data.get('destino_reserva')}, para el día {form.cleaned_data.get('fecha_reserva')} a las {form.cleaned_data.get('hora_reserva')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                            'msg_exito': msg_exito})
            
        return render(request, self.template_name, {"form": form})
   
class ReservaDelete(DeleteView):
    model = Reserva
    success_url = "/reservas/
