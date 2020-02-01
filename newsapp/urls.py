from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls import include, url


urlpatterns = [
    path('articles/<str:word>/', article_detail, name='article_det')
]