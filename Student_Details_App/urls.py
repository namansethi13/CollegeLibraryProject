from django.contrib import admin

from django.urls import path,include
from . import views
urlpatterns = [
path('',views.studentinfo,name="studentinfo"),
path('removestudent/<int:id>',views.removestudent,name="removestudent"),
    # path('filterbook',views.filterbook,name="filterbook"),
    # path('modifybook',views.modifybook,name="modifybook"),
    # # path('modifybook/<int:id>',views.modifybook,name="modifybook"),
     path('updatestudent/<int:id>',views.modify,name="modify"),
     path('addstudent',views.addstudent,name="addstudent"),
     path('showbookdetails/<int:id>',views.showbookdetails,name="showbookdetails"),
     path('payfine/<int:id>',views.payfine,name="payfine"),
     path('finalpay/<int:id>',views.finalpay,name="finalpay")
]
