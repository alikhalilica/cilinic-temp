from django.contrib import admin
from .models import Patient,HelthDepartment

class PatientAdmin(admin.ModelAdmin):
    list_display = ["name","contact",]



# Register your models here.
admin.site.register(HelthDepartment)
admin.site.register(Patient,PatientAdmin)


