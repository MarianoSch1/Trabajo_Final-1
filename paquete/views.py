from django.shortcuts import render
from django.views import View
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django.views import generic
from .models import Paquete
from .forms import PaqueteForm

class AltaPaquete(View):
    
    form_class = PaqueteForm
    template_name = 'paquete/paquete.html'
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
