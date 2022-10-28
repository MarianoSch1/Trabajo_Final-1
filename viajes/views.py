from django.shortcuts import render
from viajes.models import Reserva, vuelos
from viajes.forms import Buscar, PaqueteForm
from django.views import View
from viajes.forms import Buscar, ReservaForm, vueloForm

def mostrar_reserva(request):
  lista_reservas = Reserva.objects.all()
  return render(request, "viajes/reservas.html", {"lista_reservas": lista_reservas})

def mostrar_vuelos(request):
  lista_vuelos = vuelos.objects.all()
  return render(request, "viajes/vuelos.html", {"lista_vuelos": lista_vuelos})


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
    initial = {"nombre":"", "fecha_reserva":"", "hora_reserva":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito la reserva de {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                            'msg_exito': msg_exito})
            
        return render(request, self.template_name, {"form": form})

class AltaPaquete(View):
    
    form_class = PaqueteForm
    template_name = 'viajes/alta_paquete.html'
    initial = {"destino":"", "fecha_ida":"", "fecha_vuelta":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se ha agregado al carrito su paquete turistico a {form.cleaned_data.get('destino')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                            'msg_exito': msg_exito})
            
        return render(request, self.template_name, {"form": form})

class AltaVuelo(View):
    
    form_class = vueloForm
    template_name = 'viajes/alta_vuelo.html'
    initial = {"destino":"", "fecha_vuelo":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se ha reservado su vuelo a {form.cleaned_data.get('destino')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                            'msg_exito': msg_exito})
            
        return render(request, self.template_name, {"form": form})