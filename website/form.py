from django import forms
from django.core import validators
from website.models import Ticket

class ContactForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ["name","email",'phone_number',"body"]
    
    def clean_botcatcher(self):
            botcatcher = self.cleaned_data['botcatcher']
            if len(botcatcher) > 0:
                raise forms.ValidationError("Gotcha BOT")
            return botcatcher



