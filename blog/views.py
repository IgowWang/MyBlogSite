from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.views import generic
# Create your views here.

class BlogIndex(generic.ListView):
    template_name = "bloghome.html"
    paginate_by =2
