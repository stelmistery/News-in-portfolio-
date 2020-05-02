from django.urls import path
from django.conf.urls import include, url
from .views import *


urlpatterns = [
    path('panel/subcategory/list', subcat_list, name='subcat_list'),
    path('panel/subcategory/add', subcat_add, name='subcat_add'),
]
