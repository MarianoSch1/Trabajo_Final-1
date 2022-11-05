from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from paquete.models import Paquete
from django import forms


class PaqueteForm(forms.ModelForm):
    class Meta:
        model = Paquete
        fields = ['destino', 'fecha_ida', 'fecha_vuelta']
        widgets = {
            'fecha_ida': DatePickerInput(format='%d-%m-%y'),
            'fecha_vuelta': DatePickerInput(format='%d-%m-%y'),
        }