from django.shortcuts import render
from django.http import JsonResponse
from .models import BlogPost
from .form import ArticleForm


def articles(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            print('form is valid')
        else:
            print(form.cleaned_data)

    form = ArticleForm()
    return render(request, "blog/article.html", {'form': form})


def api(request):
    article = {'firstname': 'Bruno', 'lastname': 'Mehddeb', 'age': 48}
    return JsonResponse(article)
