# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Question'), (1, 'Answer'), (2, 'Book')]),
        ),
    ]
