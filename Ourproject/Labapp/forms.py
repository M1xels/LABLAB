from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import register1



class StaffRegistration(UserCreationForm):
    class Meta:
        model= register1
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'Job_description']
       
        

class instructorRegistration(UserCreationForm):
    class Meta:
        model = register1
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2', 'Job_description']

        
        