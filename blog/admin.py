from django.contrib import admin

from .models import *
from django_markdown.admin import MarkdownModelAdmin
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=('user_name','email','created_time')
    search_fields=['user_name']

class ArticlesAdmin(MarkdownModelAdmin):
    list_display=('title','class_name','publish_time')
    search_fields=['title']

admin.site.register(User,UserAdmin)
admin.site.register(Tag)
admin.site.register(Classification)
admin.site.register(Articles,ArticlesAdmin)
admin.site.register(Comment,MarkdownModelAdmin)


