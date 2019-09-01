from django.shortcuts import render
from .models import Blogs
# Create your views here.

def allblogs(request):
    blogs = Blogs.objects
    return render(request, 'allblogs.html', {'blogs' : blogs})
