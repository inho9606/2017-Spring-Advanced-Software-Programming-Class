# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-29 05:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipsi', '0003_apply_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='sat_year',
            field=models.IntegerField(max_length=200),
        ),
        migrations.AlterField(
            model_name='susi',
            name='gpa',
            field=models.FloatField(),
        ),
    ]
