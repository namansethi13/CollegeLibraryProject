
from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from .models import Book
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .forms import Bookform
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from Book_Lending_App.models import BookLending
from Student_Details_App.models import Student
from django.contrib import messages


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
            return redirect('/books')

            

        except:
            return HttpResponse('Unable to delete  ')
    return redirect('/books')

@login_required(login_url="/user/login/")
def modify(request,id):
     modify=Book.objects.get(b_id=id)
     form=Bookform(request.POST or None,instance=modify )
     if form.is_valid():
          form.save()
          return redirect('/books')


     books=Book.objects.all()
     context={
        'books':books,
        'form':form
    }
     return render(request,'updatebook.html',context)

@login_required(login_url="/user/login/")
def addbook(request):
    if request.method=='POST':
        bookcode=request.POST['bookcode']
        namebook=request.POST['bookname']
        
        author=request.POST['author']
        
        desc=request.POST['desc']
        if Book.objects.filter(code=bookcode).exists():
            messages.info(request, 'Book code already exists.')
            return redirect('/books')

        else:

            new_book=Book(code=bookcode,title=namebook,author=author,description=desc)
        
            new_book.save()
            return redirect('/books')

    elif request.method=='GET':
        return render(request,'addbook.html')

    else:
        return HttpResponse(request,'errror occured')

@login_required(login_url="/user/login/")
def issuebook(request,bid,id):
    enrlno=id
    book_id=bid
    book=Book.objects.get(b_id=book_id)
    try:
        Studen=Student.objects.get(enrollment_no=enrlno)
        newinst=BookLending(student=Studen,book=book)
        newinst.save()
        book.is_issued = True
        book.save()
        messages.info(request,'Book issued')
        return redirect('/books')

    except Exception as e:
        messages.info(request,'No student found. Please recheck the enrollment number')
        return HttpResponseRedirect("/books/")

def showstudentdetails(request, id):
    book_lending = get_object_or_404(BookLending, book_id=id)
    student = book_lending.student
    context = {
        'student': student
    }
    return render(request, 'student_details.html', context)
def issueanotherbook(request,id):
    
    books = Book.objects.filter(is_issued=False)
    context = {
        'books': books,
        'id':id
    }
    return render(request, 'issueanotherbook.html', context)

    
def issueforstudent(request,bid,sid):
    
    Studen=Student.objects.get(id_number=sid)
    print(Studen)
    book=Book.objects.get(b_id=bid)
    newinst=BookLending(student=Studen,book=book)
    newinst.save()
    book.is_issued = True
    book.save()
    print("saved the entry")
    return redirect('/books')

    

    
    
def returnbook(request,id):
    book=Book.objects.get(b_id=id)
    book.is_issued=False
    book.save()
    booklend=BookLending.objects.get(book=book)
    student=booklend.student
    student.totalfine=booklend.fine
    student.save()
    booklend.delete()
    return redirect('/books')
    



# def search_books(request):
#     query = request.GET.get('search')
#     if query:
#         books = Book.objects.filter(title__icontains=query)
#     else:
#         books = []
#     context = {'books': books, 'query': query}
#     return render(request, 'search_results.html', context)

        

def searchbook(request):
    if request.method == "POST":
        searched = request.POST['search']
        print(searched)
        books = Book.objects.filter(
            Q(code__icontains=searched) |       # Search in the 'code' field
            Q(title__icontains=searched) |      # Search in the 'title' field
            Q(author__icontains=searched))     # Search in the 'author' field
             
        
        context = {
            'books': books
        }
    else:
        context = {}

    return render(request, 'viewbooks.html', context)



    

