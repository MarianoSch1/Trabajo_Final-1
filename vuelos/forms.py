from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from vuelos.models import Vuelos

class VueloForm(forms.ModelForm):
    class Meta:
        model = Vuelos
        fields = ['destino' , 'fecha_vuelo']
        widgets = {
            'fecha_vuelo': DatePickerInput(format='%d-%m-%y'),}