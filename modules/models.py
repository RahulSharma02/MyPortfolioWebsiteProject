from django.db import models

# Create your models here.


class Review(models.Model):

    email = models.EmailField()
    name = models.CharField(max_length=30)
    suggestion = models.TextField()

    def __str__(self):
        return self.name




class Contact(models.Model):

    name = models.CharField(max_length=30)
    email = email = models.EmailField()
    phone = models.CharField(max_length=30)
    address = models.TextField(max_length=100)
    comments = models.TextField(max_length=100)

    def __str__(self):
        return self.name