from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect

@login_required(login_url="/user/login/")
def homeview(request):
    return render(request,'index.html')
