from django.db import models
from django.conf import settings


# class Add_to:
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


# голосование
class Poll(models.Model):
    question = models.TextField()
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)

    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count
# голосование


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
    photo = models.ImageField(upload_to='news/%Y/%m-%d/', blank=True)
    text = models.TextField(default='')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'


class Conference(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(default='')
    date = models.CharField(max_length=100)
    place = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'конференция'
        verbose_name_plural = 'конференции'