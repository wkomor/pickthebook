# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20151008_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='questiontype',
            name='type',
            field=models.IntegerField(default=1),
        ),
    ]
