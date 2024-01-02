from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=50)
    cateogry=models.CharField(max_length=50)

    def __str__(self):
        return self.title
    


class BookIssue(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    returned = models.BooleanField(default=False)

    

