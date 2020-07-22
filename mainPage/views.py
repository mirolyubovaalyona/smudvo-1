from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from account.models import *

def index(request):
    conference = Conference.objects.all()
    news = News.objects.all()
    users = Profile.objects.all()
    ads = Ads.objects.all()
    poll = Poll.objects.all()


    return render(request, "index.html", {"users": users, "news": news, "conference": conference, "ads": ads, "polls": poll})

def users(request):

    users=Profile.objects.all()
    return render(request, 'users.html', {'users':users})

def news(request):
    news=News.objects.all()
    return render(request, 'news.html', {'news':news})

def conference(request):
    conference=Conference.objects.all()
    return render(request, 'conference.html', {'conference':conference})

def ads(request):
    ads=Ads.objects.all()
    return render(request, 'ads.html', {'ads':ads})

def polls(request):
    polls=Poll.objects.all()
    return render(request, 'polls.html', {'polls':polls})


