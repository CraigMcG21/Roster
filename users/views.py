from multiprocessing import context
from telnetlib import LOGOUT
from django.shortcuts import render
from .forms import NewUserForm, EmployeeForm, RosterForm
from django.contrib.auth.decorators import login_required
from .models import Employee, Roster


def login(request):
    return render(request, 'users/login.html')


@login_required(login_url='/user/login/')
def dashboard(request):
    context = {
        'user': request.user
    }
    return render(request, 'users/dashboard.html', context)

@login_required(login_url='/user/login/')
def register(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST or None)
        if form.is_valid():
            form.save()
    form = EmployeeForm()
    context = {
        'employees': Employee.objects.all(),
        'form': form
    }
    return render(request, 'users/add_employee.html', context)



def logout(request):
    return render(request, 'users/logout.html')

def employees(request):
    context = {
        'employees': Employee.objects.all()
    }
    return render(request, 'users/employee.html', context)

def roster(request):
    if request.method == 'POST':
        form = RosterForm(request.POST or None)
        if form.is_valid():
            form.save()

    context = {
        'form': RosterForm,
        'rosters': Roster.objects.filter(),
        
        
    }
    return render(request, 'users/roster.html', context)

        