from django.shortcuts import render
from django.http import JsonResponse
from .models import BlogPost


def articles(request):
    blogs = BlogPost.objects.all()
    return render(request, "blog/article.html", context={'blogs': blogs})

def api(request):
    article = {'firstname': 'Bruno', 'lastname': 'Mehddeb', 'age': 48}
    return JsonResponse(article)
