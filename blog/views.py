from django.shortcuts import render


def articles(request):
    return render(request, "blog/index.html")
