# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cast', models.CharField(max_length=50, verbose_name=b'ator')),
                ('photo', models.ImageField(upload_to=b'media/photo', verbose_name=b'foto')),
                ('country', models.CharField(max_length=50, verbose_name=b'pais')),
            ],
            options={
                'ordering': ['cast'],
                'verbose_name': 'ator',
                'verbose_name_plural': 'atores',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genre', models.CharField(max_length=50, verbose_name=b'genero')),
            ],
            options={
                'ordering': ['genre'],
                'verbose_name': 'genero',
                'verbose_name_plural': 'generos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('movie', models.CharField(max_length=150, verbose_name=b'filme')),
                ('slug', models.SlugField(unique=True, max_length=100, blank=True)),
                ('poster', models.ImageField(upload_to=b'media/poster', verbose_name=b'poster')),
                ('synopsis', models.TextField(max_length=350, verbose_name=b'sinopse')),
                ('cast', models.ForeignKey(related_name='movie_cast', verbose_name=b'ator', to='managerfilms.Cast')),
                ('genre', models.ForeignKey(related_name='movie_genre', verbose_name=b'genero', to='managerfilms.Genre')),
            ],
            options={
                'ordering': ['movie'],
                'verbose_name': 'filme',
                'verbose_name_plural': 'filmes',
            },
            bases=(models.Model,),
        ),
    ]
