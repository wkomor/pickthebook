# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_question_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ancestor',
            name='ancestor',
        ),
        migrations.RemoveField(
            model_name='descendant',
            name='descendant',
        ),
        migrations.AddField(
            model_name='question',
            name='parent',
            field=models.ForeignKey(related_name='child', verbose_name=b'\xd0\xa0\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c', blank=True, to='books.Question', null=True),
        ),
        migrations.DeleteModel(
            name='Ancestor',
        ),
        migrations.DeleteModel(
            name='Descendant',
        ),
    ]
