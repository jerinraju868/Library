from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100,unique=True,null=False)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Books(models.Model):
    title = models.CharField(max_length=200,unique=True, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    summary = models.TextField()
    published_date = models.DateField()

    def __str__(self):
        return self.title