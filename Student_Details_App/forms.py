from socket import fromshare
from django import forms
from django.forms import ModelForm
from .models import Student
#create problem form lfor adding problems to the databse from the user side 
class Studentform(ModelForm):
    class Meta:
        model=Student
        fields="__all__"

