# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20151009_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='questiontype',
            name='description',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
