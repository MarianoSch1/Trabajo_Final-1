from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from vuelos.models import Vuelos

class Buscar(forms.Form):
    nombre_pasajero = forms.CharField(max_length=100)

class VueloForm(forms.ModelForm):
    class Meta:
        model = Vuelos
        fields = ['nombre_pasajero', 'destino' , 'fecha_vuelo_ida' , 'fecha_vuelo_vuelta', 'id']
        widgets = {
            'fecha_vuelo_ida': DatePickerInput(format='%d-%m-%y'),
            'fecha_vuelo_vuelta': DatePickerInput(format='%d-%m-%y'),
        }
