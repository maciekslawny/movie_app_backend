from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from .models import Movie, Person
from .serializers import MovieSerializer, PersonSerializer

from django_filters.rest_framework import DjangoFilterBackend


class MoviesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["id", "title"]
    queryset = Movie.objects.all().order_by("title")


class ActorsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Person.objects.filter(kind="actor").order_by("name")
    serializer_class = PersonSerializer


class DirectorsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Person.objects.filter(kind="director").order_by("name")
    serializer_class = PersonSerializer
