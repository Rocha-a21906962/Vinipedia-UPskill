# Generated by Django 3.1.7 on 2021-07-04 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0002_auto_20210704_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
    ]
