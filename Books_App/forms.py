from socket import fromshare
from django import forms
from django.forms import ModelForm
from .models import Book
#create problem form lfor adding problems to the databse from the user side 
class Bookform(ModelForm):
    class Meta:
        model=Book
        fields="__all__"

