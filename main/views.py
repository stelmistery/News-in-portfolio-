from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from newsapp.models import Article


def index(request):
    articles = Article.objects.all()
    return render(request, 'main/home.html', {"articles": articles})


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')


def panel(request):
    return render(request, 'back/home.html')
