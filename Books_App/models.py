from django.db import models

class Book(models.Model):
    b_id=models.AutoField(primary_key=True)
    code = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    is_issued=models.BooleanField(default=False)

    def __str__(self):
        return self.title
