from re import template
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html') , name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html') , name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('employee/', views.employees, name='employee'),
    path('roster/', views.roster, name='add_employee'),

]
