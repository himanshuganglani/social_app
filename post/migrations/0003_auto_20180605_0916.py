# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-05 09:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(default='jfas', max_length=200),
            preserve_default=False,
        ),
    ]
