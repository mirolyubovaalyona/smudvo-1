from django.contrib import admin
from django.urls import path
from .views import index
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', index),
    path('users', views.users, name='users'),
    path('news', views.news, name='news'),
    path('conference', views.conference, name='conference'),
    path('ads', views.ads, name='ads'),
    path('polls', views.polls, name='polls'),
]