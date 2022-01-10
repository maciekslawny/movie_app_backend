from ratings.models import Rating
from rest_framework import serializers

from .models import Movie, Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):

    get_ratings_amount = serializers.ReadOnlyField()
    get_ratings_average = serializers.ReadOnlyField()
    get_cast_actors = PersonSerializer(many=True, read_only=True)
    get_cast_directors = PersonSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"
