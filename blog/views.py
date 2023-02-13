from django.shortcuts import render
from .models import BlogPost


def articles(request):
    return render(request, "blog/article.html", context={'title': BlogPost.title})
