from django.shortcuts import render
from .forms import NewUserForm

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
        