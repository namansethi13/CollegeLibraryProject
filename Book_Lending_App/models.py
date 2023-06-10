from django.db import models
from Books_App.models import Book
from Student_Details_App.models import Student
from django.utils import timezone



from . import views

class BookLending(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField(default=timezone.now)
    due_date = models.DateField()
    fine = models.IntegerField(default=0)

    # def save(self, *args, **kwargs):
    #     # Set the due date as 15 days from the issue date
    #     self.due_date = self.issue_date + timezone.timedelta(days=15)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.name} - {self.book.title}"


