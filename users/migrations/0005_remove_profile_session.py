# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-07 09:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180607_0943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='session',
        ),
    ]
