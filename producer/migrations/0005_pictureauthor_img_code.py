# Generated by Django 3.1.7 on 2021-03-31 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producer', '0004_auto_20210330_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='pictureauthor',
            name='img_code',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
    ]
