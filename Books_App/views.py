
from django.shortcuts import render,HttpResponse,redirect
from .models import Book
from django.db.models import Q
#from .forms import bookform
def index(request):
    return render(request,'index.html')

