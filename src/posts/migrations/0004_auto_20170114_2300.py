# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-14 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20170114_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='read_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
