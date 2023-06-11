from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    
    
    path('addbook',views.addbook,name="addbook"),
    # path('viewbooks',views.viewbooks,name="viewbooks"),
    #path('removebook',views.removebook,name="removebook"),
     path('removebook/<int:id>',views.removebook,name="removebook"),
    # path('filterbook',views.filterbook,name="filterbook"),
    # path('modifybook',views.modifybook,name="modifybook"),
    # # path('modifybook/<int:id>',views.modifybook,name="modifybook"),
     path('updatebook/<int:id>',views.modify,name="modify"),
     path('issuebook/<int:bid>/<str:id>',views.issuebook,name="issuebook"),
     path('showstudentdetails/<int:id>',views.showstudentdetails,name="showstudentdetails"),
     path('showstudentdetails/issueanotherbook/<int:id>',views.issueanotherbook,name="issueanotherbook"),
     path('issueforstudent/<int:bid>/<int:sid>',views.issueforstudent,name="issueforstudent"),
     path('returnbook/<int:id>',views.returnbook,name="returnbook"),
     path('searchbook',views.searchbook,name="searchbook"),


]
