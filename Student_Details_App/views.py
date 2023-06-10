from django.shortcuts import render
from .models import Student
from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from .forms import Studentform
from Book_Lending_App.models import BookLending

# Create your views here.
def studentinfo(request):
    students=Student.objects.all()
    context={
        'students':students
    }
    return render(request,'viewstudents.html',context)
def removestudent(request,id=0):
    if id:
        try:
            remove=Student.objects.get(id_number=id)
            remove.delete()
            return redirect('/students')

            

        except:
            return HttpResponse('Unable to delete  ')
    return redirect('/students')
def modify(request,id):
     modify=Student.objects.get(id_number=id)
     form=Studentform(request.POST or None,instance=modify )
     if form.is_valid():
          form.save()
          return redirect('/students')


     students=Student.objects.all()
     context={
        'students':students,
        'form':form
    }
     return render(request,'update.html',context)
def addstudent(request):
    if request.method=='POST':
        enrollno=request.POST['enno']
        name=request.POST['studentname']
        #print(bookname)#debug
        email=request.POST['email']
        #price=int(request.POST['price'])
        phone=request.POST['phone']
        #discount=int(request.POST['discount'])
        new_student=Student(enrollment_no=enrollno,name=name,email=email,phone_number=phone)
        
        new_student.save()
        return redirect('/students')

    elif request.method=='GET':
        return render(request,'addstudent.html')

    else:
        return HttpResponse(request,'errror occured')
# def showbookdetails(request,id):
#     entry=Student.objects.get(id_number=id)
#     print(entry.enrollment_no)
#     newentry=BookLending.objects.get(student=entry.id_number)
#     print(newentry)
#     return HttpResponse(request,'done occured')
# def dashboard(request):
#     books_of_student = BookLending.objects.filter(student=request.user.id)
        #print(events_of_ngo)

        # print(request.user.ngomodel.event_set.all())
    #     return render(request,'dashboard.html',context={"events_list": events_of_ngo})
    # else:
    #     return redirect(reverse_lazy('login'))
# def showbookdetails(request, student_id):
#     student = Student.objects.get(id_number=student_id)
#     book_lendings = BookLending.objects.filter(student=student)
#     context = {
#         'student': student,
#         'book_lendings': book_lendings
#     }
#     print(student)
#     print(book_lendings)
#     return render(request, 'book_details.html', context)
def showbookdetails(request, id):
    student = Student.objects.get(id_number=id)
    book_lendings = BookLending.objects.filter(student=student)
    context = {
        'student': student,
        'book_lendings': book_lendings
    }
    print(student)
    print(book_lendings)
    return render(request, 'book_details.html', context)

