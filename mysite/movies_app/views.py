from .models import Movie, Person
from .serializers import MovieSerializer
from rest_framework import generics
from .serializers import MovieSerializer, PersonSerializer

class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pass

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ActorsList(generics.ListCreateAPIView):
    queryset = Person.objects.filter(kind='actor')
    serializer_class = PersonSerializer
    pass

class DirectorsList(generics.ListCreateAPIView):
    queryset = Person.objects.filter(kind='director')
    serializer_class = PersonSerializer
    pass

class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    

    