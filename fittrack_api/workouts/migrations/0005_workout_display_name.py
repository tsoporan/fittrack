# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 22:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0004_exercise_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='display_name',
            field=models.CharField(blank=True, help_text='A human easy to read/share name for workout', max_length=15, null=True, unique=True),
        ),
    ]
