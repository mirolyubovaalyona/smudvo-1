# Generated by Django 2.2.8 on 2020-07-23 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_poll_questions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Polls_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='')),
                ('user_id', models.IntegerField(default=0)),
                ('polls_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Polls_questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('polls_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Polls_secret',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0)),
                ('polls_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Poll_questions',
        ),
    ]