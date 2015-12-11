# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managerfilms', '0002_auto_20151211_1310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='cast',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
        migrations.AddField(
            model_name='movie',
            name='cast_list',
            field=models.ManyToManyField(to='managerfilms.Cast'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movie',
            name='genre_list',
            field=models.ManyToManyField(to='managerfilms.Genre'),
            preserve_default=True,
        ),
    ]
