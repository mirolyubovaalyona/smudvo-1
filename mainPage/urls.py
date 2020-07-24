from django.contrib import admin
from django.urls import path
from .views import index
from .views import newsPage
from .views import page_scientists
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index),
    path('newsPage', newsPage, name='newsPage'),
    path('page_scientists', page_scientists, name='page_scientists'),
]
