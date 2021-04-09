# Generated by Django 3.1.7 on 2021-04-07 23:57

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('producer', '0005_pictureauthor_img_code'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Grape',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='images/grapes/')),
                ('img_author', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='producer.pictureauthor')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='images/wines/')),
                ('pageviews', models.IntegerField(default=0)),
                ('price', models.CharField(choices=[('unknown', 'Unknown'), ('economic', 'Economic'), ('reasonable', 'Reasonable'), ('expensive', 'Expensive')], default='unknown', max_length=255)),
                ('grapes', models.ManyToManyField(to='wine.Grape')),
                ('img_author', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='producer.pictureauthor')),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producer.producer')),
                ('types', models.ManyToManyField(blank=True, related_name='wines', to='wine.Tag')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('score', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluations', to=settings.AUTH_USER_MODEL)),
                ('wine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluations', to='wine.wine')),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]