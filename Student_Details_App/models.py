from django.db import models

class Student(models.Model):
    id_number = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    
    









