# Generated by Django 3.1.7 on 2021-03-24 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producer',
            options={'ordering': ('name',)},
        ),
    ]
