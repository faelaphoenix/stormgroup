# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managerfilms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='cast',
            field=models.ManyToManyField(to='managerfilms.Cast', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(to='managerfilms.Genre', blank=True),
            preserve_default=True,
        ),
    ]
