from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
from django.views import generic
from .forms import CreateArticleForm

# Create your views here.

def blog_index(request):
    all_blogs = models.Articles.objects.all().order_by('-publish_time')
    all_class = models.Classification.objects.all()
    context={
        "blogs" : all_blogs,
        "classes":all_class
    }

    return render(request,"bloghome.html",context)


def content(request,blog_id):

    content = models.Articles.objects.get(id=blog_id)
    all_class = models.Classification.objects.all()


    context ={
        "blog":content,
        "classes":all_class
    }

    return render(request,"article.html",context)

def classification(request,class_id):
    cate = models.Classification.objects.get(id=class_id)
    articles = models.Articles.objects.filter(class_name=cate)
    all_class = models.Classification.objects.all()

    context={
        "blogs" : articles,
        "classes":all_class
    }

    return render(request,"bloghome.html",context)

def createArticle(request):

    all_class = models.Classification.objects.all()
    form = CreateArticleForm(request.POST or None)
    context={
    "classes":all_class,
    "form":form
    }
    if request.POST:
        print(request.POST['title'])
        if form.is_valid():
            form.save()


    return render(request,'create.html',context)

