# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-14 22:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='read_time',
            field=models.TextField(blank=True, null=True),
        ),
    ]
