
from django.contrib import admin

from django.urls import path,include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/',include('Books_App.urls')),
    path('user/', include('user.urls'))
    
]
