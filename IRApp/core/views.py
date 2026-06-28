'''Views para a API REST'''
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Books, Movies, Music
from .serializer import UserSerializer, BooksSerializer, MoviesSerializer, MusicSerializer

class UserView(APIView):
    '''View para o modelo User'''
    serializer_class = UserSerializer

    def get(self, _request):
        '''Retorna todos os utilizadores'''
        detail = [
            {"name": obj.name, "password": obj.password}
            for obj in User.objects.all()
        ]
        return Response(detail)

    def post(self, request):
        '''Cria um novo utilizador'''
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

class BooksView(APIView):
    '''View para o modelo Books'''
    serializer_class = BooksSerializer

    def get(self, _request):
        '''Retorna todos os livros'''
        detail = [
            {"title": obj.title, "author": obj.author,
             "year": obj.year, "genre": obj.genre, "language": obj.language}
            for obj in Books.objects.all()
        ]
        return Response(detail)

    def post(self, request):
        '''Cria um novo livro'''
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

class MoviesView(APIView):
    '''View para o modelo Movies'''
    serializer_class = MoviesSerializer

    def get(self, _request):
        '''Retorna todos os filmes'''
        detail = [
            {"title": obj.title, "director": obj.director,
             "year": obj.year, "genre": obj.genre,
             "country": obj.country, "cast": obj.cast,
             "producer": obj.producer, "format": obj.format,
             "language": obj.language}
            for obj in Movies.objects.all()
        ]
        return Response(detail)

    def post(self, request):
        '''Cria um novo filme'''
        serializer = MoviesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

class MusicView(APIView):
    '''View para o modelo Music'''
    serializer_class = MusicSerializer

    def get(self, _request):
        '''Retorna todas as músicas'''
        detail = [
            {"title": obj.title, "artist": obj.artist, "year": obj.year,
             "genre": obj.genre, "sub_genre": obj.sub_genre, "album": obj.album,
             "songs_list": obj.songs_list, "format": obj.format}
            for obj in Music.objects.all()
        ]
        return Response(detail)

    def post(self, request):
        '''Cria uma nova música'''
        serializer = MusicSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
