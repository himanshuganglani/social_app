# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-08 07:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friendlist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendrequest',
            name='user',
        ),
        migrations.AddField(
            model_name='friendrequest',
            name='user_id',
            field=models.IntegerField(null=True),
        ),
    ]
