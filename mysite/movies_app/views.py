from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Movie, Person
from .serializers import MovieSerializer, PersonSerializer


class Movies(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pass


class Actors(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Person.objects.filter(kind="actor")
    serializer_class = PersonSerializer
    pass


class Directors(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Person.objects.filter(kind="director")
    serializer_class = PersonSerializer
    pass
