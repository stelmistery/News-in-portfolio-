from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('panel/category/list', cat_list, name='cat_list'),
    path('panel/category/add', cat_add, name='cat_add'),
]
