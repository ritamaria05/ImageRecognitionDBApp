'''Modelos da base de dados'''
from django.db import models

class User(models.Model):
    '''Modelo de utilizador'''
    objects = models.Manager()
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Books(models.Model):
    '''Modelo de livros'''
    objects = models.Manager()
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    genre = models.CharField(max_length=100)
    language = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} - {self.author} - {self.year}"

class Movies(models.Model):
    '''Modelo de filmes'''
    objects = models.Manager()
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    year = models.IntegerField()
    genre = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    cast = models.CharField(max_length=100, null=True, blank=True)
    producer = models.CharField(max_length=100, null=True, blank=True)
    format = models.CharField(max_length=100) #dvd, bluray, digital, 4k...
    language = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} - {self.director} - {self.year}"

class Music(models.Model):
    '''Modelo de música'''
    objects = models.Manager()
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    year = models.IntegerField()
    genre = models.CharField(max_length=100)
    sub_genre = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    songs_list = models.CharField(max_length=100, null=True, blank=True)
    format = models.CharField(max_length=100) #cd, vinyl, digital...

    def __str__(self):
        return f"{self.title} - {self.artist} - {self.year}"
