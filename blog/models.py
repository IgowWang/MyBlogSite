from django.db import models
import datetime
from django.utils import timezone
from django_markdown.models import MarkdownField
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
class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published=True)
#博客
class Entry(models.Model):
    title = models.CharField(max_length=200)
    body = MarkdownField()
    slug = models.SlugField(max_length=200,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    objects = EntryQuerySet.as_manager()
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(day=1)

    class Meta:
        verbose_name = 'Blog Entry'
        verbose_name_plural = 'Blog Entries'
        ordering = ["-created_at"]

#评论
class Comment(models.Model):
    ID = models.CharField(max_length=50,primary_key=True)
    comment = MarkdownField()
    created_at = models.DateTimeField('created date')


    def __str__(self):
        return self.comment

    def was_published_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(day=1)
