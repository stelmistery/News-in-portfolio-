from django.shortcuts import render, get_object_or_404, redirect
from .models import Article

# Create your views here.


def article_detail(request, word):
    article = Article.objects.get(name=word)
    return render(request, 'main/article.html', {'article': article})


def articles_list(request):
    articles = Article.objects.all()
    return render(request, 'back/articles_list.html', {'articles': articles})


def articles_add(request):

    return render(request, 'back/articles_add.html')
