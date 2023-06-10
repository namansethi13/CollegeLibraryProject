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
     path('issuebook/<int:id>',views.issuebook,name="issuebook"),
     path('issuebook/submit_enrollment',views.submit_enrollment,name="submit_enrollment"),
     path('showstudentdetails/<int:id>',views.showstudentdetails,name="showstudentdetails")
]
