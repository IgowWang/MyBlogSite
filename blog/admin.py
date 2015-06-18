from django.contrib import admin

from .models import *
from django_markdown.admin import MarkdownModelAdmin
# Register your models here.

admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Classification)
admin.site.register(Articles,MarkdownModelAdmin)
admin.site.register(Comment,MarkdownModelAdmin)


