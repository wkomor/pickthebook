# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-14 10:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0009_auto_20161119_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slag',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=16, null=True),
        ),
    ]