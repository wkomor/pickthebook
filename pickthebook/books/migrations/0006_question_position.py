# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_questiontype_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='position',
            field=models.IntegerField(default=0),
        ),
    ]
