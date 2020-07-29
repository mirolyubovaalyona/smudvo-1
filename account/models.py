from django.db import models
from django.conf import settings


# голосование
class Polls(models.Model):
    title = models.TextField()

    # def total(self):
        # return self.option_one_count + self.option_two_count + self.option_three_count
        # return
# голосование


class Polls_questions(models.Model):
    poll = models.ForeignKey(Polls, default=None, on_delete=models.CASCADE)
    question = models.TextField(max_length=200, default='')
    count = models.IntegerField(default=0)


class Polls_secret(models.Model):
    poll = models.ForeignKey(Polls, default=None, on_delete=models.CASCADE)
    user_id = models.IntegerField()


class Polls_comment(models.Model):
    polls_id = models.IntegerField()
    user_id = models.IntegerField()
    content = models.TextField(default='')


class User_mas(models.Model):
    name = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.CharField(max_length=100, default='')


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m-%d/', blank=True)
    organization = models.CharField(max_length=200, default='')
    position = models.CharField(max_length=200, default='')
    bio = models.TextField(default='')
    scientist = models.NullBooleanField(default=False)
    user_is_reject = models.NullBooleanField(default=False)
    user_submit = models.NullBooleanField(default=False)

    scopus = models.CharField(max_length=100, default='')
    wos = models.CharField(max_length=100, default='')
    e_library = models.CharField(max_length=100, default='')
    instagram = models.CharField(max_length=100, default='')
    facebook = models.CharField(max_length=100, default='')
    vk = models.CharField(max_length=100, default='')
    google_scholar = models.CharField(max_length=100, default='')

    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'профили'


class Ads(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='ads/%Y/%m-%d/', blank=True)
    text = models.TextField(default='')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'ад'
        verbose_name_plural = 'адс'


class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(default='')


    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'

class Images (models.Model):
    news = models.ForeignKey(News, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news/%Y/%m-%d/', null=True, blank=True)

    def __str__(self):
        return self.news.title + " Img"


class Conference(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(default='')
    date_begin = models.CharField(max_length=100)
    date_end = models.CharField(max_length=100)
    place = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='conference/%Y/%m-%d/', blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'конференция'
        verbose_name_plural = 'конференции'