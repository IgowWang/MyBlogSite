from django.db import models

# Create your models here.

#用户
class User(models.Model):
    ID = models.CharField(max_length=50,primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    admin = models.BooleanField(default=0)
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=500)
    created_at = models.DateTimeField('created date')
#博客
class Blog(models.Model):
    ID = models.CharField(max_length=50,primary_key=True)
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=200)
    blog_content = models.TextField()
    created_at = models.DateTimeField('created date')
    
    def __str__(self):
        return self.content

#评论
class Comment(models.Model):
    ID = models.CharField(max_length=50,primary_key=True)
    comment = models.TextField()
    created_at = models.DateTimeField('created date')
    
    
    def __str__(self):
        return self.comment
        