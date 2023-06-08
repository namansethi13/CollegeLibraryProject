
from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from .models import Book
from django.db.models import Q
from .forms import Bookform
from django.urls import reverse
from django.contrib.auth.decorators import login_required


@login_required(login_url="/user/login/")
def index(request):
    books=Book.objects.all()
    context={
        'books':books
    }
    #print(context)
    return render(request,'viewbooks.html',context)

@login_required(login_url="/user/login/")
def removebook(request,id=0):
    if id:
        try:
            remove=Book.objects.get(b_id=id)
            remove.delete()
            return render(request,'viewbooks.html')

            

        except:
            return HttpResponse('Unable to delete  ')
    return render(request,'viewbooks.html')

@login_required(login_url="/user/login/")
def modify(request,id):
     modify=Book.objects.get(b_id=id)
     form=Bookform(request.POST or None,instance=modify )
     if form.is_valid():
          form.save()
          return HttpResponseRedirect(reverse('index'))

     books=Book.objects.all()
     context={
        'books':books,
        'form':form
    }
     return render(request,'update.html',context)

@login_required(login_url="/user/login/")
def addbook(request):
    if request.method=='POST':
        bookcode=request.POST['bookcode']
        namebook=request.POST['bookname']
        #print(bookname)#debug
        author=request.POST['author']
        #price=int(request.POST['price'])
        desc=request.POST['desc']
        #discount=int(request.POST['discount'])
        new_book=Book(code=bookcode,title=namebook,author=author,description=desc)
        # new_book.save()
        #image=request.FILES.get('image')
        # if image:
        #     return HttpResponse('uploaded sucessfully')
        # else:
        #     return HttpResponse('error in uploading img')
        
        
        
        # price=int(request.POST['price'])
        # desc=request.POST['desc']
        # discount=int(request.POST['discount'])
        # new_book=book(name=namebook,author_name=aname,price=price,description=desc,discount=discount)
        new_book.save()
        return HttpResponseRedirect(reverse('index'))
    elif request.method=='GET':
        return render(request,'addbook.html')

    else:
        return HttpResponse(request,'errror occured')




    

