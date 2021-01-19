from django.http import HttpResponse,HttpResponseRedirect
from . models import HelthDepartment , Patient
from . forms import PatientForm
from django.shortcuts import render,redirect,get_objects_or_404
#import requests



# Create your views here.
# Retrieve
def index(request):
    #categories = Category.objects.all()
    patients = Patient.objects.all()
    form = PatientForm()
    context = {"patients":patients,"form":form}
    return render(request,"index.html",context)

    # Delete
def delete(request,id):
    patient = Patient.objects.get(id=id)
    patient.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# update
def edit(request,id):
    patients = Patient.objects.all()
    #selected_patient = patients.objects.get(id=id)
    selected_patient = get_objects_or_404(Patient,id=id)
    if request.method == "GET":   
        form = PatientForm(instance=selected_patient)
        context = {"patients":patients,"form":form ,"selected_patient":selected_patient}
        return render(request,"edit.html",context)
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid:
            #print(form.__dict__)
            selected_patient.name = form.data["name"]
            selected_patient.contact = form.data["contact"]
            selected_patient.email = form.data["email"]
            selected_patient. booking_date = form.data[" booking_date"]
            selected_patient.appointment_date = form.data["appointment_date"]
            selected_patient.helth_department = form.data["helth_department"]
            selected_patient.history = form.data["historyl"]
            selected_patient.save()
       
        return redirect("/")





# Insert
def add_(request):
    if request.method=="POST":
        form = PatientForm(data=request.POST)
        if form.is_valid():
            
            form.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
       