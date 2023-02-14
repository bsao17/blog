from django.shortcuts import render
from .models import BlogPost


def articles(request):
    blogs = BlogPost.objects.all()
    return render(request, "blog/article.html", context={'blogs': blogs})
