from django.db import models

class Book(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
