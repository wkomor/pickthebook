# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20160502_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
    ]