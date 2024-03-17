from django.db import models

# Create your models here.
# models.py

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE) # 저자 하나에 책은 여러개일 수도 있음

    def __str__(self):
        return self.title
