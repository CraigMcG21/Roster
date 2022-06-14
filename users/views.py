from telnetlib import LOGOUT
from django.shortcuts import render
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST or None)
        if form.is_valid():
            form.save()

    form = NewUserForm()
    return render(request, 'users/register_user.html', {'form': form})


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
        form = NewUserForm(request.POST or None)
        if form.is_valid():
            form.save()

    form = NewUserForm()
    return render(request, 'users/add_employee.html')



def logout(request):
    return render(request, 'users/logout.html')

        