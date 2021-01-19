from .models import Patient
from django import forms


class PatientForm (forms.ModelForm):
    class Meta : 
        model = Patient
        fields = '__all__'
    