# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20151008_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ancestor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Descendant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='treepath',
            name='ancestor',
        ),
        migrations.RemoveField(
            model_name='treepath',
            name='descendant',
        ),
        migrations.RemoveField(
            model_name='question',
            name='type',
        ),
        migrations.AddField(
            model_name='questiontype',
            name='question',
            field=models.ForeignKey(default=1, to='books.Question'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Treepath',
        ),
        migrations.AddField(
            model_name='descendant',
            name='descendant',
            field=models.ForeignKey(related_name='+', to='books.Question'),
        ),
        migrations.AddField(
            model_name='ancestor',
            name='ancestor',
            field=models.ForeignKey(related_name='+', to='books.Question'),
        ),
    ]
