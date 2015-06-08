from django.db import models
import datetime
from django.utils import timezone
#Create your models here.

#用户
class User(models.Model):
    ID = models.CharField(max_length=50,primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    admin = models.BooleanField(default=0)
    name = models.CharField(max_length=50)
    image = models.ImageField()
    created_at = models.DateTimeField('created date')
#博客
class Entrpy(models.Model):
    ID = models.CharField(max_length=50,primary_key=True)
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=200)
    entrpy = models.TextField()
    created_at = models.DateTimeField('created date')

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(day=1)
#评论
class Comment(models.Model):
    ID = models.CharField(max_length=50,primary_key=True)
    comment = models.TextField()
    created_at = models.DateTimeField('created date')


    def __str__(self):
        return self.comment

    def was_published_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(day=1)
