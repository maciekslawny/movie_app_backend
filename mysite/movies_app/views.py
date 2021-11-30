from django.shortcuts import render
import requests
from .models import Movie, Person
from .serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializers import MovieSerializer

class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pass

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer




# def add_movies_to_db(request):
#     '''Geting top 20 movies data from API and adding to database'''
#     response = requests.get('https://api.themoviedb.org/3/movie/popular?api_key=ad616d70a03f15fd5c01caf1b27911b0&language=en-US&page=1')
#     popular_movies = response.json()

#     for movie in popular_movies['results']:
#         print(movie['title'], movie['release_date'])

        
#         if Movie.objects.filter(api_id=movie['id']):
#             print(movie['title'], 'JUZ W BAZIe')
#             continue

#         Movie.objects.create(
#             title=movie['title'],
#             release_date= 2000,
#             poster_url= movie['poster_path'],
#             description= movie['overview'][:400],
#             api_id = movie['id'],
#         )

#     return render(request, 'movies_list.html')



    

    