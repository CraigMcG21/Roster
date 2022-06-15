from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Employee, Roster
from django import forms


# User form
class NewUserForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'placeholder': 'Username'}), required=True)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), required=True)
    password2 = forms.CharField(label='Confirm', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}), required=True)


    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class EmployeeForm(forms.ModelForm):
    name_f = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'x-model': 'event_date', 'class': 'bg-gray-200 appearance-none border-2 border-gray-200 rounded-lg w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-blue-500'}))
    name_l = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'x-model': 'event_date', 'class': 'bg-gray-200 appearance-none border-2 border-gray-200 rounded-lg w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-blue-500'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'x-model': 'event_date', 'class': 'bg-gray-200 appearance-none border-2 border-gray-200 rounded-lg w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-blue-500'}))
    phone = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'x-model': 'event_date', 'class': 'bg-gray-200 appearance-none border-2 border-gray-200 rounded-lg w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-blue-500'}))
    pin = forms.CharField(max_length=4, widget=forms.TextInput(attrs={'x-model': 'event_date', 'class': 'bg-gray-200 appearance-none border-2 border-gray-200 rounded-lg w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-blue-500'}))

    class Meta:
        model = Employee
        fields = ('name_f', 'name_l', 'email', 'phone', 'pin')

class RosterForm(forms.ModelForm):
    employee_id = forms.ModelChoiceField(queryset=Employee.objects.all(), widget=forms.Select(attrs={'class': 'bg-gray-200 appearance-none border-2 border-gray-200 rounded-lg w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-blue-500'}))
    date = forms.DateField(widget=forms.TextInput(attrs={'x-model': 'event_date', 'class': 'bg-gray-200 appearance-none border-2 border-gray-200 rounded-lg w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-blue-500'}))
    start_time = forms.TimeField(widget=forms.TextInput(attrs={ 'class': 'bg-gray-200 appearance-none border-2 border-gray-200 rounded-lg w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-blue-500'}))
    end_time = forms.TimeField(widget=forms.TextInput(attrs={ 'class': 'bg-gray-200 appearance-none border-2 border-gray-200 rounded-lg w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-blue-500'}))

    class Meta:
        model = Roster
        fields = ('date', 'employee_id', 'start_time', 'end_time')


