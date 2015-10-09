# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20151009_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='child', verbose_name=b'\xd0\xa0\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c', blank=True, to='books.Question', null=True),
        ),
    ]
