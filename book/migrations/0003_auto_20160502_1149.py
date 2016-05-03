# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20160502_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_positive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='item',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
