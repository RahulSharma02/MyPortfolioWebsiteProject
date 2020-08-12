from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

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


# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     date_posted = models.DateTimeField(default=timezone.now)
#     author = models.ForeignKey(User,on_delete=models.CASCADE)
#
#     def __str__(self):
#        return self.title
#     #
    # def get_absolute_url(self):
    #     return reverse('post-detail',kwargs={'pk':self.pk})