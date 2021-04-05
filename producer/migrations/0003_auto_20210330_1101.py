# Generated by Django 3.1.7 on 2021-03-30 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producer', '0002_auto_20210324_1925'),
    ]

    operations = [
        migrations.CreateModel(
            name='PictureAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('author_url', models.URLField(blank=True)),
                ('link_name', models.CharField(max_length=100)),
                ('picture_url', models.URLField(blank=True, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='producerpicture',
            name='img_author',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='producer.pictureauthor'),
        ),
    ]
