from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls import include, url


urlpatterns = [
    path('articles/<str:word>/', article_detail, name='article_det'),
    path('panel/articles/list/', articles_list, name='articles_list'),
    path('panel/articles/add/', articles_add, name='articles_add'),
]