from django.contrib import admin

from .models import User,Entry,Comment
from django_markdown.admin import MarkdownModelAdmin
# Register your models here.


class EntryAdmin(MarkdownModelAdmin):
    list_display = ("title","created_at")
    prepopulated_fields ={"slug":("title",)}

admin.site.register(Entry,EntryAdmin)
admin.site.register(User,MarkdownModelAdmin)
admin.site.register(Comment,MarkdownModelAdmin)


