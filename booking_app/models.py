from django.db import models

# Create your models here.

class HelthDepartment(models.Model):
    name = models.CharField(max_length=100)
    availability = models.DateTimeField()
    def __str__(self):
        return self.name

#helth_department = ((0,"daily task"),(1,"work jobs"),(2,"house needs"))

class Patient(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.EmailField()
    booking_date = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    appointment_date = models.DateTimeField(null=True , blank=True)
    #appointment_time = models.TimeField(null=True , blank=True)
    helth_department = models.ForeignKey(HelthDepartment,on_delete=models.CASCADE,null=True) 
    history = models.TextField()
    #patient_contact = models.PhoneField()
    #helth_department = models.PositiveSmallIntegerField(choices=helth_department,default=0)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-booking_date"]
