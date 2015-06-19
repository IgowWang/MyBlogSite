from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.views import generic
# Create your views here.

def blog_index(request):

    return render(request,"bloghome.html",{})
