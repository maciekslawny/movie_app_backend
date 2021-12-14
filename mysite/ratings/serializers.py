from rest_framework import serializers

from .models import Rating


class RatingSerializer(serializers.ModelSerializer):

    ratings_amount = serializers.SerializerMethodField()
    ratings_average = serializers.SerializerMethodField()

    def get_ratings_amount(self, obj):
        ratings_list = Rating.objects.filter(movie=obj.movie)
        ratings_amount = len(ratings_list)
        return ratings_amount

    def get_ratings_average(self, obj):
        ratings_list = Rating.objects.filter(movie=obj.movie)
        average_value = sum([rating.value for rating in ratings_list]) / len(
            ratings_list
        )
        return average_value

    class Meta:
        model = Rating
        fields = "__all__"
