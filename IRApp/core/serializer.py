'''Serializer para os modelos do core'''
from rest_framework import serializers
from core.models import User, Books, Movies, Music

class UserSerializer(serializers.ModelSerializer):
    '''Serializer para o modelo User'''
    class Meta:
        '''Meta class for UserSerializer'''
        model = User
        fields = ['name', 'password']

class BooksSerializer(serializers.ModelSerializer):
    '''Serializer para o modelo Books'''
    class Meta:
        '''Meta class for BooksSerializer'''
        model = Books
        fields = ['title', 'author', 'year', 'genre', 'language']

class MoviesSerializer(serializers.ModelSerializer):
    '''Serializer para o modelo Movies'''
    class Meta:
        '''Meta class for MoviesSerializer'''
        model = Movies
        fields = ['title', 'director', 'year', 'genre',
                  'country', 'cast', 'producer', 'format', 'language']

class MusicSerializer(serializers.ModelSerializer):
    '''Serializer para o modelo Music'''
    class Meta:
        '''Meta class for MusicSerializer'''
        model = Music
        fields = ['title', 'artist', 'year', 'genre',
                  'sub_genre', 'album', 'songs_list', 'format']
