# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 12:24
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20160502_1215'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='item',
            managers=[
                ('_default_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='level',
        ),
    ]
