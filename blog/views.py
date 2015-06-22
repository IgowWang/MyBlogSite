from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.views import generic
# Create your views here.

def blog_index(request):
    all_blogs = models.Articles.objects.all().order_by('-publish_time')

    context={
        "blogs" : all_blogs
    }


    return render(request,"bloghome.html",context)
