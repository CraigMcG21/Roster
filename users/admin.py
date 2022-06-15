from django.contrib import admin

# Register your models here.

from .models import Employee, Roster

admin.site.register(Employee)
admin.site.register(Roster)
