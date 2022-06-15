from datetime import date
from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name_f = models.CharField(max_length=100)
    name_l = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    pin = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_f + " " + self.name_l


class Roster(models.Model):
    roster_id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.employee_id.name_f + " " + self.employee_id.name_l

    
