from .models  import Profile
from django.shortcuts import render,get_object_or_404
from django.http  import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
specialCharacters = "~!@#$%^&*_-+=`|\()/{/}[]:;'<>,.?/"

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        # print(username,email)
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return HttpResponseRedirect(reverse('users:register'))
            elif len(password) <8:
                messages.info(request,'ATLEAST 8 CHARACTER PASSWORD NEEDED')
                return HttpResponseRedirect(reverse('users:register'))
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Taken By a User')
                return HttpResponseRedirect(reverse('users:register'))
            elif(any(char.isalpha() for char in password) == False):
                messages.info(request,"ERROR: password must contain at least letter")
                return HttpResponseRedirect(reverse('users:register'))
            elif(any(char.isupper() for char in password) == False):
                messages.info(request,"ERROR: password must contain at least one uppercase character")
                return HttpResponseRedirect(reverse('users:register'))
            elif(any(char.islower() for char in password) == False):
                messages.info(request,"ERROR: password must contain at least one lowercase character")
                return HttpResponseRedirect(reverse('users:register'))
            elif(any(char.isdigit() for char in password) == False):
                messages.info(request,"ERROR: password must contain at least one digit")
                return HttpResponseRedirect(reverse('users:register'))
            elif all(x not in specialCharacters for x in password):
                messages.info(request,"ERROR: password must contain at least one special character")
                return HttpResponseRedirect(reverse('users:register'))
            else:
                entry=User.objects.create_user(username=username,email=email,password=password)
                entry.save()
                messages.success(request,'Account Created!')
                return HttpResponseRedirect(reverse('users:login'))
        else:
            messages.info(request,'Password and confirm password didn"t match')
            return HttpResponseRedirect(reverse('users:register'))
    return render(request,'signup.html')

def logout(request):
    auth_logout(request)
    messages.success(request,'Logout Successful')
    return HttpResponseRedirect('/')