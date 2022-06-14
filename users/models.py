from django.db import models

# Create your models here.

class Emplooyee(models.Model):
    name_f = models.CharField(max_length=100)
    name_l = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    pin = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)