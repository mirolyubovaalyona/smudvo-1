# Generated by Django 2.2.8 on 2020-07-29 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_auto_20200729_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polls_questions',
            name='question',
            field=models.TextField(default='', max_length=200),
        ),
    ]