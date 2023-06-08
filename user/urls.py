from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

app_name='users'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('login/',(auth_view.LoginView.as_view(template_name='login.html')),name='login')
]