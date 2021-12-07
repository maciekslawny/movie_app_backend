from .models import Movie, Person
from .serializers import MovieSerializer, PersonSerializer
from rest_framework import viewsets

class Movies(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pass

class Actors(viewsets.ModelViewSet):
    queryset = Person.objects.filter(kind='actor')
    serializer_class = PersonSerializer
    pass

class Directors(viewsets.ModelViewSet):
    queryset = Person.objects.filter(kind='director')
    serializer_class = PersonSerializer
    pass