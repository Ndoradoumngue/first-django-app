# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-08 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='choice_title',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='question_title',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
