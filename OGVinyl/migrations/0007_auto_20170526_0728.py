# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-26 05:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OGVinyl', '0006_auto_20170525_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='release',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
