from django.db import models

class Student(models.Model):
    id_number = models.AutoField(primary_key=True, max_length=20)
    enrollment_no=models.CharField(max_length=12)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    totalfine=models.IntegerField(default=0)
    def __str__(self):
        return self.name



    
    









