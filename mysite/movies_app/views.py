from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Movie, Person
from .serializers import MovieSerializer, PersonSerializer


class MoviesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Movie.objects.all().order_by('title')
    serializer_class = MovieSerializer


class ActorsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Person.objects.filter(kind="actor").order_by('name')
    serializer_class = PersonSerializer


class DirectorsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Person.objects.filter(kind="director").order_by('name')
    serializer_class = PersonSerializer
