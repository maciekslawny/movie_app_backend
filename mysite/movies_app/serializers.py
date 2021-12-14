from ratings.models import Rating
from rest_framework import serializers

from .models import Movie, Person


class MovieSerializer(serializers.ModelSerializer):

    ratings_amount = serializers.SerializerMethodField()
    ratings_average = serializers.SerializerMethodField()
    cast_actors = serializers.SerializerMethodField()
    cast_directors = serializers.SerializerMethodField()

    def get_ratings_amount(self, obj):
        ratings_list = Rating.objects.filter(movie=obj.id)
        ratings_amount = len(ratings_list)
        return ratings_amount

    def get_ratings_average(self, obj):
        ratings_list = Rating.objects.filter(movie=obj.id)
        average_value = 0
        try:
            average_value = sum([rating.value for rating in ratings_list]) / len(
                ratings_list
            )
        except:
            pass
        return average_value

    def get_cast_actors(self, obj):
        actors = []
        persons_list = [x for x in obj.crew.all()]
        for x in persons_list:
            if x.kind == "actor":

                nowy = {
                    "name": f"{x.name}",
                    "id": f"{x.id}",
                    "path": f"{x.profile_path}",
                }

                actors.append(nowy)
        return actors

    def get_cast_directors(self, obj):
        directors = []
        persons_list = [x for x in obj.crew.all()]
        for x in persons_list:
            if x.kind == "director":

                nowy = {
                    "name": f"{x.name}",
                    "id": f"{x.id}",
                    "path": f"{x.profile_path}",
                }

                directors.append(nowy)
        return directors

    class Meta:
        model = Movie
        fields = "__all__"


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"
