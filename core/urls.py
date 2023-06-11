
from django.contrib import admin

from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    

    path('books/', include(('Books_App.urls', 'Books_App'), namespace='Books_App')),
    path('user/', include('user.urls')),
    
    path('students/',include('Student_Details_App.urls'))
    
]
