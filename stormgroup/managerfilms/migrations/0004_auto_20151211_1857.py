# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managerfilms', '0003_auto_20151211_1628'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='cast_list',
            new_name='casts',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='genre_list',
            new_name='genres',
        ),
        migrations.AddField(
            model_name='genre',
            name='slug',
            field=models.SlugField(unique=True, max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
