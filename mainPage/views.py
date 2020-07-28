from django.shortcuts import render
from django.http import HttpResponse
from account.models import *


def index(request):
    conference = Conference.objects.all()
    news = News.objects.all()
    users = Profile.objects.all()
    ads = Ads.objects.all()
    poll = Polls.objects.all()
    poll_comment = Polls_comment.objects.all()
    poll_questions = Polls_questions.objects.all()
    return render(request, "index.html", {"users": users, "news": news, "conference": conference, "ads": ads, "polls": poll, "comment": poll_comment, "questions": poll_questions})

def newsPage(request, news_id):
    try:
        news = News.objects.get(id=news_id)
    except:
        raise Http404("Новость не найдена")


    img_list=news.images_set.all()
    return render(request, "newsPage.html", {"new": news, "img_list": img_list})

def page_scientists(request):
    conference = Conference.objects.all()
    news = News.objects.all()
    users = Profile.objects.all()
    ads = Ads.objects.all()
    poll = Polls.objects.all()
    return render(request, "page_scientists.html", {"users": users, "news": news, "conference": conference, "ads": ads, "polls": poll})