# Generated by Django 3.1.7 on 2021-04-01 01:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wine', '0013_auto_20210331_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='score',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]