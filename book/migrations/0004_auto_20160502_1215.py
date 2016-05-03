# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20160502_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='author',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Question'), (1, 'Answer'), (2, 'Book')], db_index=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(db_index=True, max_length=255),
        ),
    ]
