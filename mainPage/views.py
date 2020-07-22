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

