from django.shortcuts import render, get_object_or_404, redirect
from .models import Article

# Create your views here.


def article_detail(request, word):
    article = Article.objects.get(name=word)
    return render(request, 'main/article.html', {'article': article})
