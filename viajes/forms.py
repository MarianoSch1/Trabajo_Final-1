from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from django import forms
from viajes.models import Reserva

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100)

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nombre' , 'fecha_reserva' , 'hora_reserva']
        widgets = {
            'fecha_reserva': DatePickerInput(format='%d-%m-%y'),
            'hora_reserva': TimePickerInput(),
        }