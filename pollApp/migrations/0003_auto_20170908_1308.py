# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-08 13:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollApp', '0002_auto_20170908_0922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='choice_title',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_title',
        ),
    ]
