from django.db import models
import datetime
from django.utils import timezone
from django_markdown.models import MarkdownField
from ckeditor.fields import RichTextField
#Create your models here.

#博客标签
class Tag(models.Model):
    tag_name = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.tag_name
#分类，类名
class Classification(models.Model):
    class_name = models.CharField(max_length=20)

    def __str__(self):
        return self.class_name

#用户
class User(models.Model):
    user_name = models.CharField(max_length=50,unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    image = models.ImageField(blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name

#博客
class Articles(models.Model):
    #标题
    title = models.CharField(max_length=50,verbose_name='标题')
    #内容
    content = RichTextField(verbose_name="内容")
    #发表时间
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    #分类
    class_name = models.ForeignKey(Classification,verbose_name='类别')
    #标签
    tags = models.ManyToManyField(Tag,blank=True,verbose_name='标签')


    def __str__(self):
        return self.title

#评论
class Comment(models.Model):
    comment = RichTextField()
    publish_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,verbose_name='user_name',null=True,blank='')

    belong_to = models.ForeignKey(Articles,verbose_name='title',null=True,blank='')
    def __str__(self):
        return self.comment

