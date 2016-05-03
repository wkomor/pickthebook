# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20151008_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questiontype',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='type',
            field=models.ForeignKey(default=True, to='books.QuestionType'),
            preserve_default=False,
        ),
    ]
