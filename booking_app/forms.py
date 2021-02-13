from .models import Patient
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'
class PatientForm (forms.ModelForm):
    class Meta : 
        model = Patient
        fields = '__all__'
        widgets = {
            'appointment_date': DateInput(),
            #'appointment_time': TimeInput(),
        }
    
