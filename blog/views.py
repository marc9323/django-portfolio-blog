from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs':blogs})

#blog_id captured in urls url path
def detail(request, blog_id):
    #specify model and primary key
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':detailblog})


