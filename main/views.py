from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404


def index(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')
