# -*- coding: utf-8 -*-
# project by Rafaela Santos
from django.db import models


class Cast(models.Model):

    """Modelo tabela de atores"""

    cast = models.CharField('ator', max_length=50)
    photo = models.ImageField('foto', upload_to='media/photo')
    country = models.CharField('pais', max_length=50)

    class Meta:
        ordering = ['cast']
        verbose_name = 'ator'
        verbose_name_plural = 'atores'

    def __unicode__(self):  # Python 2
        return self.cast


class Genre(models.Model):

    """Modelo tabela de generos dos filmes"""

    genre = models.CharField('genero', max_length=50)

    class Meta(object):
        ordering = ['genre']
        verbose_name = 'genero'
        verbose_name_plural = 'generos'

    def __unicode__(self):  # Python 2
        return self.genre


class Movie(models.Model):

    """Modelo tabela de filmes"""

    movie = models.CharField('filme', max_length=150)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    poster = models.ImageField('poster', upload_to='media/poster')
    synopsis = models.TextField('sinopse', max_length=350)
    genres = models.ManyToManyField(Genre)
    casts = models.ManyToManyField(Cast)

    class Meta:
        ordering = ['movie']
        verbose_name = 'filme'
        verbose_name_plural = 'filmes'

    def __unicode__(self):  # Python 2
        return self.movie
