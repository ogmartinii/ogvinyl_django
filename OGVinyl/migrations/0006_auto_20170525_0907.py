# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-25 07:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OGVinyl', '0005_auto_20170525_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='line_up',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='note',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
